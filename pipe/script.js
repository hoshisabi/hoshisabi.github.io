// --- New Scramble and Goal Definitions ---

// New Scrambled State (UL, UR, DR, UR) -> [3, 0, 1, 0]
// Requires at least 3 moves to solve.
const SCRAMBLED_STATE = [3, 0, 1, 0]; 

// New Goal State (The 'Circle' / 'C' shape) -> [1, 2, 0, 3]
// TL(DR), TR(DL), BL(UR), BR(UL)
const GOAL_STATE = [1, 2, 0, 3]; 

let pipes = [...SCRAMBLED_STATE];
const messageEl = document.getElementById('message');
const resetButton = document.getElementById('reset-button');
const pipeElements = [
    document.getElementById('pipe-0'),
    document.getElementById('pipe-1'),
    document.getElementById('pipe-2'),
    document.getElementById('pipe-3')
];

// --- Core Game Logic ---

function rotatePipe(pipeIndex) {
    // Clockwise rotation: index advances (e.g., 3 -> 0)
    pipes[pipeIndex] = (pipes[pipeIndex] + 1) % 4;
}

function updateDisplay() {
    let solved = checkWin(); // Check the win status once

    for (let i = 0; i < 4; i++) {
        const rotationClass = `rotate-${pipes[i]}`;
        // Base class is always 'pipe'
        let classList = ['pipe', rotationClass];
        
        // Add the 'solved' class if the puzzle is complete
        if (solved) {
            classList.push('solved');
        }
        
        // Apply all classes
        pipeElements[i].className = classList.join(' ');
    }
    
    if (solved) {
        // Display WIN message
        messageEl.textContent = "SOLVED! The circle is complete!";
        messageEl.classList.add('win-message');
        resetButton.style.display = 'block';
    } else {
        // Display regular message
        messageEl.textContent = "Find the solution!";
        messageEl.classList.remove('win-message');
        resetButton.style.display = 'none';
    }
}

function checkWin() {
    // Check if the current state array matches the goal state array
    return pipes.every((val, index) => val === GOAL_STATE[index]);
}

function resetGame() {
    pipes = [...SCRAMBLED_STATE];
    updateDisplay();
}

// --- Button Actions (Mapping the moves) ---

function topRotate() {
    rotatePipe(0); // TL
    rotatePipe(1); // TR
    updateDisplay();
}

function bottomRotate() {
    rotatePipe(2); // BL
    rotatePipe(3); // BR
    updateDisplay();
}

function leftRotate() {
    rotatePipe(0); // TL
    rotatePipe(2); // BL
    updateDisplay();
}

function rightRotate() {
    rotatePipe(1); // TR
    rotatePipe(3); // BR
    updateDisplay();
}

// Initialize the display on load
updateDisplay();