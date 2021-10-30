
#! ---------------------------------------
#? 89. Python Dictionaries

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# Retrieving items from dictionary.
print(programming_dictionary["Function"])

# Adding new items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again."

#Create an empty dictionary.
empty_dictionary = {}

#Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

#Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

#Loop through a dictionary
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])

#! ---------------------------------------
#? 90. Exercise - Grading Program

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]

    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)

#! ---------------------------------------
#? 91. Nesting Lists and Dictionaries

#Nesting
import os
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

#Nesting a List in a Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting Dictionary in a Dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

#Nesting Dictionaries in Lists
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },
]

#! ---------------------------------------
#? 92. Exercise - Dictionary in List

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

def add_new_country(country_visited, times_visited, cities_visited):
    travel_log.append(
        {
            "country": country_visited, 
            "visits": times_visited, 
            "cities": cities_visited
        }
    )

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

#! ---------------------------------------
#? 93. Day 9 Project - The Secret Auction Program

import os
def clear(): return os.system('cls') 
# use 'clear()' in code to clear screen.
from Day9_auction_art import logo

print(logo + "\n")
print("Welcome to The Secret Auction program!")
other_bidders = "yes"
auction_log = {}

def find_highest_bidder(bidding_record):
  highest_bid = 0
  highest_bidder = ""
  # bidding_record = auction_log
  for bidder in bidding_record:
    bid = bidding_record[bidder]
    if bid > highest_bid:
      highest_bid = bid
      highest_bidder = bidder
  print(f"The highest bidder is {highest_bidder} with a bid of ${highest_bid}")

while other_bidders == "yes":
    bidder_name = input("What is your name?: ")
    bid_amt = int(input("what's your bid?: $"))
    auction_log[bidder_name] = bid_amt

    other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ")
    if other_bidders == "yes":
        clear()

find_highest_bidder(auction_log)

# todo My alternate solution to check max bidder using 'max' function
# highest_bidder = max(auction_log, key=auction_log.get)
# highest_bid = auction_log[highest_bidder]
# print(f"{highest_bidder} wins the auction with a bid of ${highest_bid}")
