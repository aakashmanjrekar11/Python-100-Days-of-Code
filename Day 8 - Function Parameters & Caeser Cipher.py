
# #! -----------------------------------
# #? 79. Functions with Inputs

# #* Parameter - Name of data
# #* Argument - Actual value of data

# def greet_with_name(name):  # 'name' is the Parameter 
#     print(f"Hey {name}")
#     print(f"How you doing {name}")

# greet_with_name("John") # "John" is the Argument

# #! -----------------------------------
# #? 80. Positional Vs. Keyword Arguments

# # Functions with more than 1 input
# def greet_with(name, location):
#   print(f"Hello {name}")
#   print(f"What is it like in {location}?")

# # Positional Arguments
# greet_with("Jack Bauer", "Nowhere")
# #vs.
# greet_with("Nowhere", "Jack Bauer")

# # Keyword Arguments
# greet_with(location="London", name="Angela")

# #! -----------------------------------
# #? 81. Exercise - Paint Area Calculator

# import math
# def paint_calc(height, width, cover):
#   number_of_cans = math.ceil((height * width) / cover)
#   print(f"You'll need {number_of_cans} cans of paint.")

# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

# #! -----------------------------------
# #? 82. Exercise - Prime Number Checker

# def prime_checker(number):
#   is_prime = True

#   for i in range(2, number):
#     if number % i == 0:
#       is_prime = False

#   if is_prime == False:
#     print(f"{number} is prime.")
#   else:
#     print(f"{number} is a prime number.")

# n = int(input("Check this number: "))
# prime_checker(number=n)

#! -----------------------------------
#? 83-86. Caesar Cipher

from Day8_CaesarCipher_art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")

print(logo)

should_end = False

while not should_end:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")

