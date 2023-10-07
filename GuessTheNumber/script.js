const secretNumber = Math.floor(Math.random() * 100) + 1;
let attempts = 0;

const guessInput = document.getElementById("guessInput");
const guessSubmit = document.getElementById("guessSubmit");
const message = document.querySelector(".message");

guessSubmit.addEventListener("click", checkGuess);

function checkGuess() {
    const userGuess = parseInt(guessInput.value);

    if (isNaN(userGuess) || userGuess < 1 || userGuess > 100) {
        message.textContent = "Please enter a valid number between 1 and 100.";
        return;
    }

    attempts++;

    if (userGuess === secretNumber) {
        message.textContent = `Congratulations! You guessed the number ${secretNumber} in ${attempts} attempts.`;
        guessInput.disabled = true;
        guessSubmit.disabled = true;
    } else if (userGuess < secretNumber) {
        message.textContent = "Try higher.";
    } else {
        message.textContent = "Try lower.";
    }

    guessInput.value = "";
}
