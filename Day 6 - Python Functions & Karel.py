
#? 57. Python Functions

# defining a function
def my_func():
    print("Hello")
    print("World!")

# calling a function
my_func()

#! -----------------------------------
#? 58. Reeborg's Hurdles Loop Challenge

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for n in range(1, 7):
    jump()

#! -----------------------------------
#? 59. Indentation in Python
#* For indentation use 1 tab = 4 spaces 

#! -----------------------------------
#? 60. While loops
#* refer code from '58'

while at_goal() is False:
    jump()

#! -----------------------------------
#? 61. Hurdles challenge using while loops

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    elif front_is_clear():
        move()

#! -----------------------------------
#? 62. Jumping over hurdles with variable heights

def jump():
    turn_left()
    move()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()


while not at_goal():
    if wall_in_front():
        jump()
    elif front_is_clear():
        move()

#! -----------------------------------
#? 63. Day 6 Project - Escaping The Maze

def turn_right():
    turn_left()
    turn_left()
    turn_left()

# code block for rare test cases
while front_is_clear():
    move()
turn_left()

# normal solution for simple test cases
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
