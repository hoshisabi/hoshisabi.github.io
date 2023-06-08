import csv
import re

left_file = "_data/orig_adventures.csv"
right_file = "_data/DDALDM.csv"
updated_file = "_data/adventures.csv"
keys = ["Code", "Title", "Levels", "Runtime", "RelDate", "Season", "Authors", "Tier", "Price", "Seed", "G.Ad.","Eber","RMH", "Epic", "URL"]

adventure_details = {}

# affiliate_id=171040
def replace_affiliate(s):
    if "https://www.dmsguild.com" not in s:
        return s
    elif "affiliate_id=" in s:
        return re.sub(r"affiliate_id=\d+", "affiliate_id=171040", s)
    else:
        return f"{s}?affiliate_id=171040"

with open(left_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        adventure_details[row['Code']] = row

with open(right_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        new_code = row['Code']
        if new_code in adventure_details:
            old_row = adventure_details[new_code]
            if not old_row["URL"]:
                old_row["URL"] = row["URL"]
            adventure_details[new_code] = old_row
        else:
            old_row = {'Code': new_code, 'Title': row['Title'], 'Levels': row['Levels'], 'URL': row['URL']}
        old_row["URL"] = replace_affiliate(old_row["URL"])
        old_row["RelDate"] = row["RelDate"]
        old_row["Seed"] = row["Seed"]
        old_row["Authors"] = row["Authors"]
        old_row["Season"] = row["Season"]
        old_row["Tier"] = row["Tier"]
        old_row["Price"] = row["Price"]

with open(updated_file, "w", encoding='UTF8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=keys)
    writer.writeheader()
    for row in adventure_details.values():
        writer.writerow(row)

print(adventure_details)
