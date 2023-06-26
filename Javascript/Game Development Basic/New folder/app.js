const computerChoice = document.getElementById('computer-choise')
const userChoice = document.getElementById('user-choice')
const resultDisplay = document.getElementById('result')

const possibleChoice = document.querySelectorAll('button')

possibleChoice.forEach(possibleChoice => possibleChoice.addEventListener('click', (e)))