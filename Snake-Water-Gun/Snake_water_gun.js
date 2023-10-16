console.log("*** Welcome to Snake water gun ***\n")
console.log("*** Rules ***");
console.log("1. Snake beats Water")
console.log("2. Water beats Gun")
console.log("3. Gun beats Snake")
console.log("4. You will have 5 rounds to beat the computer all the best!\n");
console.log("Enter choices like:\n-> s for snake\n-> w for water\n-> g for gun\n\n")

let playerScore = 0 , computerScore = 0 , round = 1;

while(round <=5 ){

  console.log("|| Round "+round+"||\n")
  console.log("Player- "+playerScore+" Computer- "+computerScore+"\n\n");
  

let playerChoice = prompt("Enter your choice: ")

if(playerChoice != 's' && playerChoice != 'w' && playerChoice != 'g'  ){
  console.log("You entered something different !!\nFinal Score: \n"+"Player- "+playerScore+" Computer- "+computerScore);
  break;
}

else{

  const characters = ['s','w','g'];
let x = Math.floor(Math.random() * 3)

let computerChoice = characters[x];
console.log("Your response: ",playerChoice);
console.log("Computer response: ",computerChoice);

if((playerChoice == 's' && computerChoice == 'w') || (playerChoice == 'w' && computerChoice == 'g') || (playerChoice == 'g' && computerChoice == 's') ){

  console.log("You win this round!!\n\n");
  playerScore++;
}

else if( playerChoice == computerChoice ){
  console.log("draw!!\n\n");
}
else{
  
  console.log("Computer wins this round!!\n\n")
  computerScore++;
}
  
}
  round++
}

 console.log("Final Score: \n"+"Player- "+playerScore+" Computer- "+computerScore+"\n");
if(playerScore>computerScore){
  console.log("Congrats you are the ultimate winner!!")
}

else if( playerScore == computerScore){
  console.log("It was draw overall!!")
}

else{
  console.log("Computer is the overall winner!!");
}


