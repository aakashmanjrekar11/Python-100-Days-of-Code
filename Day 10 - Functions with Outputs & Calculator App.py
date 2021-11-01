
#! -------------------------------------
#? 97. Functions with Outputs

# Functions with Outputs
def format_name(f_name, l_name):
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"{formated_f_name} {formated_l_name}"

print(format_name("aAkasH", "mANjRekaR"))

# Storing output in a variable
formatted_name = format_name(input("Your first name: "), input("Your last name: "))
print(formatted_name)

# or printing output directly
print(format_name(input("What is your first name? "), input("What is your last name? ")))

# Already used functions with outputs.
length = len(formatted_name)

#! -------------------------------------
#? 98. Multiple return values

# Return as an early exit
def format_name(f_name, l_name):
  # Docstring
  """Take a first and last name and format it 
  to return the title case version of the name."""
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs."
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"Result: {formated_f_name} {formated_l_name}"

print(format_name(input("What is your first name? "),
      input("What is your last name? ")))

#! -------------------------------------
#? 99. Exercise - Days in Month

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False


def days_in_month(check_year, check_month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  
  if check_month > 12 or check_month < 1:
      return "Invalid month!"

  if is_leap(check_year) is True:
    month_days[1] = 29
  
  return month_days[check_month - 1]

year = int(input("Enter a year in numbers: "))
month = int(input("Enter a month in numbers: "))
days = days_in_month(year, month)
print(days)

#! -------------------------------------
#? 100. Docstrings

def add(n1, n2):
    """This is a docstring. 
    The docstring should always be the first line inside the function.
    This function 'add' adds up two numbers: n1 + n2
    """
add(1, 2) # Hovering cursor over this function call shows the docstring.

#! -------------------------------------
#? 101. Calculator App

import os
def clear(): return os.system('cls') 
# use 'clear()' in code to clear screen.from art import logo
from Day10_calculator_art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()

calculator()

