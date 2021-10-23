
# #? 17. Primitive Data Types

# # String
# "Hello", "World", "123"
# # -Subscript
# print("Hello"[0])
# print("World"[2])

# # Integer
# print(123 + 456)
# print(15,000 + 11)
# # -Replacing commas(,) with underscores(_). The underscore makes the large number more readable.
# print(15_000 + 11)

# # Float
# print(3.1425)
# print(101.96)

# # Boolean
# True
# False

# #! ------------------------------------------
# #? 18. Type Error, Type Checking & Type Conversion

# # Type Errors
# len(1234) #Throws a type error as 'int' has no length

# num_char = len("Aakash")
# print("Your name has " + num_char + " characters.") #Throws a Type Error as 'str' cant be concatenated with 'int'.

# # Type Checking
# print(type(num_char)) #This prints 'int' as the datatype of num_char.
# print(type("Aakash")) #This prints 'str' as the datatype.
# print(type(float(123))) #Prints 'float' datatype.
# print(70 + float("100.5")) #Converts 'str' to 'float' and then adds 70. Result is 'float'.
# print(str(70) + str(100)) #Converts 'int' to 'str' and prints 70100.

# # Type Conversion
# new_num_char = str(num_char) #Converts 'int' to 'str'.
# print("Your name has " + new_num_char + " characters.")

# #! ------------------------------------------
# #? 19. Coding Exercise - Data Types

# two_digit_number = input("Type a two digit number: ")
# print(type(two_digit_number)) #Prints 'str' datatype
# print(int(two_digit_number[0]) + int(two_digit_number[1])) #Converts 'str' to 'int' and adds the 2 digits.

# #! ------------------------------------------
# #? 20. Math Operations

# # Addition
# print(6 + 3) # Returns 9

# # Subtraction
# print(6 - 3) # Returns 3

# # Multiplication
# print(6 * 3) # Returns 18

# # Division *** Always returns 'float'
# print(6 / 3) # Returns 2

# # Exponent
# print(2 ** 3) # Returns 8

# # PEMDAS-LR
# # Paranthesis >Exponent >Multiplication >Division >Addition >Subtraction (From Left to Right priority)
# print(3 * 3 + 3 / 3 - 3) # Prints 7.0 in 'float' cause of division
# print(3 * (3 + 3) / 3 - 3) # Prints 3.0


# #! ------------------------------------------
# #? 21. BMI Calculator Exercise

# print("Welcome to BMI Calculator!")
# height = float(input("Enter your height in metres: "))
# weight = float(input("Enter your weight in kgs: "))

# bmi = int(weight / height ** 2)
# print("Your BMI is: " + str(bmi))

# #! ------------------------------------------
# #? 22. Number Manipulation and F Strings

# # Round function
# print(round(8 / 3)) # Returns 3
# print(round(8 / 3, 2)) # Returns 2.67 
# print(round(12.82372, 3)) # Returns 12.824

# # Floor Division
# print(8 // 3) # Returns 'int' number as result

# # Math shortcuts
# score = 0
# score += 1 # Similarly, -=, *=, /=
# print(score)

# # f-strings - Converts every datatype to a 'str'.
# score = 0
# height = 1.8
# isWinning = True
# print(f"Score is {score}, Height is {height}, You are winning is {isWinning}")

#! ------------------------------------------
#? 23. Life in Weeks exercise

# print("Welcome to Life in Weeks calculator!")
# age = int(input("What is your current age?: "))

# days_left = (90 * 365) - (age * 365)
# weeks_left = (90 * 52) - (age * 52)
# months_left = (90 * 12) - (age * 12)

# print(f"You have {days_left} days, {weeks_left} weeks & {months_left} months left.")

#! ------------------------------------------
#? 24. Day 2 Project - Tip Calculator

print("Welcome to the Tip Calculator!")
bill = float(input("What was the total bill?: $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15?: "))
people = int(input("How many people to split the bill?: "))

bill_with_tip = bill + (tip / 100 * bill)
payPerPerson = "{:.2f}".format(bill_with_tip / people)

print(f"Each person should pay: ${payPerPerson}")
