
#! ------------------------------------
#? 67. Challenge 1 - Picking random words & Checking Answers

import random
from hangman_words import word_list
from hangman_art import stages, logo
import os
def clear(): return os.system('cls')

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
endOfGame = False
lives = 6

print(logo + "\n")

#Create blanks
display = []
for _ in range(word_length):
    display.append("_")
print(display)

while not endOfGame:
    guess = input("Guess a letter: ").lower()
    clear()   # clears output screen
    if guess in display:
      print(f"You've already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            endOfGame = True
            print("You've lost :(")
    
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        endOfGame = True
        print("You've won!")

    print(stages[lives])
