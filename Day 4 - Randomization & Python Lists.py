
#! --------------------------------------
#? 39. Random Module

# import random

# randomInteger = random.randint(1, 10)    # including 1 and 10
# print(randomInteger)

# randomFloat = random.random()    # between 0.0000.. to 0.9999...
# print(randomFloat)

# randomFloat2 = random.random() * 5    # between 0.000... to 4.999...
# print(randomFloat2)

#! --------------------------------------
#? 40. Exercise - Heads or Tails

# import random

# print("Welcome to Coin Flipper!")
# tossValue = random.randint(0, 1)
# # print(tossValue)
# if tossValue == 1:
#     print("Heads")
# elif tossValue == 0:
#     print("Tails")

#! --------------------------------------
#? 41. Offset and appending items to lists

# Offset - Items in a List start with 0, 1, 2....
# myList = ["a", "b", "c"]
# print(myList[0])
# print(myList[2])

# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts"]
# print(states_of_america)

# #TODO End of list starts with '-1'
# print(states_of_america[-1]) 
# print(states_of_america[-3])

# # append() - adds an object to the end of List
# states_of_america.append("dummy state") # Don't use [], as only appending single object to list
# print(states_of_america)

# # extend() - adds multiple objects to the end of List
# states_of_america.extend(["carrot, tomato, potato"]) # Use [], as adding multiple objects to list
# print(states_of_america)

#! --------------------------------------
#? 42. Exercise - Banker Roulette - Who will pay the bill?

# import random

# print("Welcome to Banker Roulette!")
# names_string = input("Give me everybody's names, separated by a comma.\n")
# names = names_string.split(", ")

# # approach 1:
# banker = random.randint(0, len(names)-1)
# print(f"{names[banker]} will pay the bill!")

# # approach 2:
# banker = random.choice(names)
# print(banker + " will pay the bill!")

#! --------------------------------------
#? 43. IndexErrors and Nested Lists

# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts"]   # 6 items, 0-5

# # IndexError: list index out of range
# #! print(states_of_america[6]) 
# #* List has 0-5, so 6 is out of range

# # Nested lists - Lists inside a List
# fruits = ["Apple", "Mango", "Grapes"]
# vegetables = ["Potato", "Tomato", "Pumpkin"]

# mix_basket = [fruits, vegetables]   # [[fruits], [vegetables]] 
# print(mix_basket)

#! --------------------------------------
#? 44. Exercise - Treasure Map

# row1 = ["⬜️", "⬜️", "⬜️"]
# row2 = ["⬜️", "⬜️", "⬜️"]
# row3 = ["⬜️", "⬜️", "⬜️"]

# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")

# position = input("Where do you want to put the treasure? Column-Row: ")

# position_CR = list(position)
# map[int(position_CR[1]) - 1] [int(position_CR[0]) - 1] = "X"

# print(f"{row1}\n{row2}\n{row3}")

#! --------------------------------------
#? 45. Day 4 Project - Rock Paper Scissors

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#todo Solution in course

game_images = [rock, paper, scissors]

user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw")

#todo My solution

userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: "))
computerChoice = random.randint(0, 2)

# user-computer combos : RR, RP, RS, PR, PP, PS, SR, SP, SS

if userChoice == 0 and computerChoice == 0:  #? RR
    print("You chose Rock!" + rock)
    print("Computer chose Rock!" + rock)
    print("It's a draw O_o")
elif userChoice == 0 and computerChoice == 1:  #? RP
    print("You chose Rock!" + rock)
    print("Computer chose Paper!" + paper)
    print("You lose *_*")
elif userChoice == 0 and computerChoice == 2:  #? RS
    print("You chose Rock!" + rock)
    print("Computer chose Scissors!" + scissors)
    print("You win! ^_^")
elif userChoice == 1 and computerChoice == 0:  # ? PR
    print("You chose Paper!" + paper)
    print("Computer chose Rock!" + rock)
    print("You win! ^_^")
elif userChoice == 1 and computerChoice == 1:  # ? PP
    print("You chose Paper!" + paper)
    print("Computer chose Paper!" + paper)
    print("It's a draw O_o")
elif userChoice == 1 and computerChoice == 2:  # ? PS
    print("You chose Paper!" + paper)
    print("Computer chose Scissors!" + scissors)
    print("You lose *_*")
elif userChoice == 2 and computerChoice == 0:  # ? SR
    print("You chose Scissors!" + scissors)
    print("Computer chose Rock!" + rock)
    print("You lose *_*")
elif userChoice == 2 and computerChoice == 1:  # ? SP
    print("You chose Scissors!" + scissors)
    print("Computer chose Paper!" + paper)
    print("You win! ^_^")
elif userChoice == 2 and computerChoice == 2:  # ? SS
    print("You chose Scissors!" + scissors)
    print("Computer chose Scissors!" + scissors)
    print("It's a draw O_o")
else:
    print("Invalid choice, you lose *_*")
