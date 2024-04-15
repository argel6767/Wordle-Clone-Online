var inputContainers = document.getElementsByClassName("user-guess-letter");
Array.from(inputContainers).forEach(function(inputContainer) {
    inputContainers.addEventListener("keyup", function(event) {
        if (inputContainer.value.length == inputContainer.maxLength) {
            inputContainer.nextElementSibling.focus();
        }
    });
});



document.getElementById('userGuess').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        submitGuess();
    }
});

function submitGuess() {
    var guessInput = document.getElementById('userGuess').value;
    var data = { 'guess': guessInput };
    
    fetch('/guess', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        // Handle response from the server (update UI, display feedback, etc.)
        console.log(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function updateGameBoard(data) {
    var currentBoard = data.currentBoard;
    var charsInWord = data.charsInWord;

    var boardContainer = document.getElementById('board');
    boardContainer.innerHTML = '';

    currentBoard.forEach(char => {
        var charElement = document.createElement('span');
        charElement.textContent = char;
        boardContainer.appendChild(charElement);
    });

    var charsInWordContainer = document.getElementById('charsInWord');
    charsInWordContainer.textContent = '';
    charsInWordContainer.textContent = 'Characters in word, but not in the right spot: ' + charsInWord.join(', ');
}