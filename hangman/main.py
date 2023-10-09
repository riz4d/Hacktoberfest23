#Completed
#Semi-self project
#Bugs fixed : 1
#Updates : 1

import random
from words import words
import string

#To select a Valid Word

def The_word():
    word=random.choice(words)
    while " " in word or "_" in word or "-" in word:
        word=random.choice(words)

    return word.upper()


#Actual code 

#Sets needed for process

word=The_word()
word_letters=set(word)
alphabets=set(string.ascii_uppercase)
used_letters=set()
lives=5

#initiating loop

while len(word_letters)>0 and lives>0:
    
  user_input=str(input("\n\nGuess your letter: ")).upper()
  print("\nyou have",lives,"lives left")

#checking if the letter can be used

  if user_input in alphabets-used_letters:
      used_letters.add(user_input)

    #getting word_letters to zero ends game

      if user_input in word_letters:
          word_letters.remove(user_input)

    #Bringing life concept
    
      else:
          lives=lives-1  
          print("\nLetter is not in word")   

  elif user_input in used_letters:
      print("\nYou have already used that letter")
  else:
      print("\nEnter a valid letter")

  #Space-Letter trick

  print("\nLettes used: "," ".join(used_letters))

  word_list=[x if x in used_letters else "-" for x in word]    
  
  print("\n"," ".join(word_list))

#Final result

if len(word_list)==0:
   print("\n\nCongrats, The word was",word)  

else:
    print("sorry you are dead.The word was",word)
