
// document.getElementById("num1-el").textContent = num1
// document.getElementById("demo").innerHTML = num2

// let sumEl = document.getElementById("sum-el")


// function Add(){
//     let result = num1 + num2
//     sumEl.textContent = "Sum: " + result
// }

// function Subtract(){
//     let result = num1 - num2
//     sumEl.textContent = "Sum: " + result
// }

// function Divide(){
//     let result = num1 / num2
//     sumEl.textContent = "Sum: " + result
// }

// function Multiply(){
//     let result = num1 * num2
//     sumEl.textContent = "Sum: " + result
    
// }

let cards = []
let sum = 0
let hasBlackJack = false // no blackjack by default
let isAlive = false
let message = ""
let messageEl = document.getElementById("message-el")
console.log(messageEl)
let sumEl = document.getElementById("sum-el")
let cardsEl = document.getElementById("cards-el")

let player = {
    name: "David",
    chips: 145
    }





let playerEl = document.getElementById("player-el")
playerEl.textContent = player.name + ": $" + player.chips


console.log(rollDice())

function getRandomCard() {
    let randomNumber = Math.floor(Math.random() * 13) + 1
    if (randomNumber === 1) {
        return 11
    } else if (randomNumber > 10) {
        return 10
    } else {
        return randomNumber
    }
}

function startGame() {
    isAlive = true
    let firstCard = getRandomCard()
    let secondCard = getRandomCard()
    cards = [firstCard, secondCard]
    sum = firstCard + secondCard
    renderGame();
}

function renderGame() {
    cardsEl.textContent = "Cards: "
    for (let i = 0; i < cards.length; i++) {
        cardsEl.textContent += cards[i] + " "
    }

    sumEl.textContent = "Sum: " + sum
    if (sum <= 20) {
        message = "Do you want to draw a new card?"
        sum = sum
    } else if (sum === 21) {
        message = "Woohoo! You've got Blackjack!"
        hasBlackJack = true
        sum = sum
    } else {
        message = "You are out of the game!"
        isAlive = false
        sum = sum
    }
    // 3. Log it out!
    messageEl.textContent = message
    
}

function newCard() {
    if (isAlive === true && hasBlackJack === false) {
        let card = getRandomCard()
        sum += card
        cards.push(card) // add to the "cards" array
        renderGame() 
    }
}
