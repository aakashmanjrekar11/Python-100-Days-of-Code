
#! --------------------------------------
#? 48. for loop

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
print(fruits)

#! --------------------------------------
#? 49. Exercise - Average Height

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# 180 124 165 173 189 169 146
print(student_heights)

# sum of heights
sum_heights = 0
for h in student_heights:
    sum_heights += h
print(sum_heights)

# total students
total_students = 0
for s in student_heights:
    total_students += 1
print(total_students)

# average height = sum / total students
avg_height = sum_heights / total_students
print(round(avg_height))

# todo alternate solution without using 'for' loop
#* sum_heights = sum(student_heights)
#* total_students = len(student_heights)
#* avg_height = round(sum_heights / total_students)

#! --------------------------------------
#? 50. Exercise - High Score

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

# 78 65 89 86 55 91 64 89
# The highest score in the class is: x

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")

#todo alternate solution without using for loop
#* print(max(student_scores))

#! --------------------------------------
#? 51. for loops and range() function

# for loop with range()
for number in range(1, 10): # Excluding 10
    print(number) # prints 1 to 9

# sum of numbers from 1 to 100
total = 0
for num in range(1, 101):
    total += num
print(total)

#! --------------------------------------
#? 52. Exercise - Adding Even Numbers from 1 to 100

total_sum_even = 0
for n in range(1, 101):
    if n % 2 == 0:
        total_sum_even += n
print(f"The sum of all even numbers from 1 to 100 is {total_sum_even}")

#todo alternate sol - using 'step' in range()
total = 0
for n in range(2, 101, 2): # starts at 2, with increment(step) of 2, ends at 100
    total += n
print(total)

#! --------------------------------------
#? 53. Exercise - FizzBuzz
# n % 3 print Fizz, n % 5 print Buzz, n % 3,5 print FizzBuzz

for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

#! --------------------------------------
#? 54. Day 5 Project - Password Generator

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#todo Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""

for l in range(1, nr_letters + 1):
    password += random.choice(letters)

for s in range(1, nr_symbols + 1):
    password += random.choice(symbols)

for n in range(1, nr_numbers + 1):
    password += random.choice(numbers)

print(password)

#todo Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []

for l in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for s in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

for n in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")

