function makeMove(col) {
    fetch('/move', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ col: col })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'win') {
            document.getElementById('status').innerText = `Player ${data.player} wins!`;
        } else if (data.status === 'continue') {
            updateBoard(data.board);
        }
    });
}

function updateBoard(board) {
    const boardElement = document.getElementById('game-board');
    boardElement.innerHTML = '';
    for (let row = 0; row < board.length; row++) {
        for (let col = 0; col < board[row].length; col++) {
            const cell = document.createElement('div');
            cell.classList.add('h-16', 'w-16', 'bg-gray-600', 'rounded-full', 'flex', 'justify-center', 'items-center', 'cursor-pointer');
            cell.setAttribute('onclick', `makeMove(${col})`);
            const disk = document.createElement('div');
            disk.classList.add('h-14', 'w-14', 'rounded-full');
            if (board[row][col] === 'R') {
                disk.classList.add('bg-red-500');
            } else if (board[row][col] === 'Y') {
                disk.classList.add('bg-yellow-500');
            } else {
                disk.classList.add('bg-gray-600');
            }
            cell.appendChild(disk);
            boardElement.appendChild(cell);
        }
    }
}
