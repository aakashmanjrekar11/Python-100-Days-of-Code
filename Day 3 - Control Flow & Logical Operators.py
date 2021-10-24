
#! ----------------------------------------------
#? 27. Control Flow with if/else & Conditional Operators (Contains '29' & '32')

# if/else control flow
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:    #? Code for '29'
        bill = 5
        print("Pay $5")
    elif age <= 18:
        bill = 7
        print("Pay $7")
    elif age >= 45 and age <= 55:   #? Code for '34'
        bill = 0
        print("Free ticket!")
    else:
        bill = 12
        print("Pay $12")

    wants_photo = input("Do you want a photo taken? Y or N: ")
    if wants_photo == "Y":    #? Code for '32'
        bill += 3

    print(f"Your final bill is {bill}")
else:
    print("Sorry, you cant ride!")

# Conditional Operators
#*   >  - Greater than
#*   <  - Less than
#*  >=  - Greater than or Equal to
#*  <=  - Less than or Equal to
#*  ==  - Equal to
#*  !=  - Not equal to

#! ----------------------------------------------
#? 28. Exercise - Odd or Even? (Modulo intro)

print("Exercise to check whether a number is odd or even!")
number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print(f"The number {number} is even!")
else:
    print(f"The number {number} is odd")

#! ----------------------------------------------
#? 29. Nested if and elif statements (Check '27' code)

#! ----------------------------------------------
#? 30. Exercise BMI 2.0

print("Welcome to BMI Calc 2.0!")
weight = float(input("enter your weight in kg: "))
height = float(input("enter your height in m: "))

bmi = round(weight / (height ** 2))
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you are normal weight")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese")
else:
    print("You are clinically obese")

#! ----------------------------------------------
#? 31.Exercise - Leap Year

#* Logic - on every year that is evenly divisible by 4 **except** every year that is evenly divisible by 100 **unless** the year is also evenly divisible by 400

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

#! ----------------------------------------------
#? 32. Multiple if statements in succession (Check '27' code)

#! ----------------------------------------------
#? 33. Exercise - Pizza Order Practice

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L : ")
add_pepperoni = input("Do you want pepperoni? Y or N : ")
extra_cheese = input("Do you want extra cheese? Y or N : ")

bill = 0
if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
elif size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill += 3
else:
    bill += 25
    if add_pepperoni == "Y":
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")

#! ----------------------------------------------
#? 34. Logical Operators (and, or, not)
#? (Check '27' code)
#* (and) T and T = T, T and F = F, F and F = F
#* (or)  T or T = T, T or F = T, F or F = F
#* (not) not T = F, not F = T

#! ----------------------------------------------
#? 35. Exercise - Love Calculator 

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_string = name1 + name2
lowercase_string = combined_string.lower()

t = lowercase_string.count("t")
r = lowercase_string.count("r")
u = lowercase_string.count("u")
e = lowercase_string.count("e")

true = t + r + u + e

l = lowercase_string.count("t")
o = lowercase_string.count("t")
v = lowercase_string.count("t")
e = lowercase_string.count("t")

love = l + o + v + e

loveScore = int(str(true) + str(love))

if (loveScore < 10) or (loveScore > 90):
    print(f"Your score is {loveScore}, you go together like coke and mentos.")
elif (loveScore >= 40) and (loveScore <= 50):
    print(f"Your score is {loveScore}, you are alright together.")
else:
    print(f"Your love score is {loveScore}")

#! ----------------------------------------------
#? 36. Day 3 Project - Treasure Island

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

LorR = input("You're at a cross road. Where do you want to go? Type 'left' or 'right': \n").lower()
if LorR == "left":
    SorW = input("You arrive at a lake. Do you want to swim across or wait for a boat? Type 'swim' or 'boat': \n").lower()
    if SorW == "boat":
        door = input("You take the boat and arrive at a shack that has 3 doors, which one do you enter? Type 'red' or 'yellow' or 'blue': \n").lower()
        if door == "yellow":
            print("You enter the main room of the shack. Here you find the treasure chest that has 1000 gold coins!! You win!!!")
        elif door == "red":
            print("You fall into a pit of fire. Game over *_*")
        elif door == "blue":
            print("You fall into a pit of snakes. Game over *_*")
        else:
            print("Please type a valid response! Game over *_*")
    elif SorW == "swim":
        print("You try to swim in the lake and get attacked by a crocodile. Game over *_*")
    else:
        print("Please type a valid response! Game over *_*")
elif LorR == "right":
    print("You arrive at a camp of bandits who lock you up. Game over *_*")
else:
    print("Please type a valid response! Game over *_*")
