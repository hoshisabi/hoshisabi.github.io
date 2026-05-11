import csv
from collections import defaultdict
import os

def read_csv(file_path):
    with open(file_path, 'r') as f:
        return list(csv.reader(f))

def read_template(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def parse_assignments(assignments):
    dm_assignments = defaultdict(list)
    headers = assignments[1][2:]  # Get the slot headers
    for row in assignments[2:]:  # Skip the first two rows
        adventure = row[0]
        tier = row[1]
        for i, slot in enumerate(row[2:], start=2):
            if slot:
                for dm in slot.split(','):
                    dm = dm.strip()
                    dm_assignments[dm].append((adventure, tier, headers[i-2]))
    return dm_assignments

def create_email_content(dm_name, assignments, email, template, adventure_links):
    assignment_list = "<ul>"
    for adventure, tier, slot in assignments:
        download_link = adventure_links.get(adventure, {}).get('download', "No download link available")
        purchase_link = adventure_links.get(adventure, {}).get('purchase', "")

        assignment_list += f"<li><strong>{adventure} {tier}</strong> - {slot}<br>"
        assignment_list += f"Download link: <a href='{download_link}'>{download_link}</a><br>"
        if purchase_link:
            assignment_list += f"Purchase link: <a href='{purchase_link}'>{purchase_link}</a><br>"
        assignment_list += "</li>"
    assignment_list += "</ul>"

    return template.format(
        dm_name=dm_name,
        assignments=assignment_list,
        email=email
    )

def generate_emails(dm_assignments, dm_lookup, template, adventure_links):
    if not os.path.exists('emails'):
        os.makedirs('emails')

    for initials, assignments in dm_assignments.items():
        dm_info = next((dm for dm in dm_lookup if dm[2] == initials), None)
        if dm_info:
            name, email, _ = dm_info
            content = create_email_content(name, assignments, email, template, adventure_links)
            filename = f"emails/{initials}_assignment.html"
            with open(filename, 'w') as f:
                f.write(content)
            print(f"Email for {name} ({initials}) has been generated.")
        else:
            print(f"No DM found with initials {initials}")

def parse_adventure_links(file_path):
    links = {}
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        for row in reader:
            links[row[0]] = {'download': row[1], 'purchase': row[2] if len(row) > 2 else ''}
    return links

def main():
    assignments = read_csv('dmassignments.csv')
    dm_lookup = read_csv('dmlookup.csv')[1:]  # Skip header row
    template = read_template('email_template.html')
    adventure_links = parse_adventure_links('adventures.csv')

    dm_assignments = parse_assignments(assignments)
    generate_emails(dm_assignments, dm_lookup, template, adventure_links)
    print("All emails have been generated in the 'emails' folder.")

if __name__ == "__main__":
    main()