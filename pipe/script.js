// The current state of the 4 pipes (0=TL, 1=TR, 2=BL, 3=BR)
// Index represents the rotation angle (0=0deg, 1=90deg, 2=180deg, 3=270deg)
// 0:UR, 1:DR, 2:DL, 3:UL
// Initial State (UL, UL, DR, DR) -> (3, 3, 1, 1)
const SCRAMBLED_STATE = [3, 3, 1, 1];

// Goal State (DR, DL, UR, UL) -> (1, 2, 0, 3)
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
    for (let i = 0; i < 4; i++) {
        const rotationClass = `rotate-${pipes[i]}`;
        // Clear previous rotation classes
        pipeElements[i].className = 'pipe ' + rotationClass;
    }
    
    if (checkWin()) {
        messageEl.textContent = "SOLVED! Great job in 3 moves!";
        messageEl.classList.add('win-message');
        resetButton.style.display = 'block';
    } else {
        messageEl.textContent = "Find the 3-move solution!";
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
