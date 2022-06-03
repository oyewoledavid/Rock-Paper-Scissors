# It was fun building this, although it's a little challenging
# The input_validation is to validate the following:
# 1 if user enter any value at all
# 2 if user enter more than one character
# 3 if the user input is a string

# The Show choice function might seem unnecessary but i could not find a better way
# to show the player and CPU input in the format specified

#Creating a seperate file for the functions is to make the main file look neat and i was just experimenting what i just learnt

# I have tried as much as possible to make this error free but i believe it's still not 100% error free
# PLEASE LEAVE A REMARK


import random
from functions import *

option = ("R", "P", "S")


def start():
    print("Welcome to Rock,Paper,Scissors")

    user_choice = input("Pick an option R(rock),P(paper),S(scissors) \n")

    input_validation(user_choice)

    while user_choice.upper() not in ["R", "P", "S"]:
        print("Please Enter a Valid Option")
        start()
    else:
        cpu_choice = random.choice(option)

        show_choice(user_choice, cpu_choice)

        if user_choice.upper() == cpu_choice:
            print("The game is a draw, lets start over")
            start()

        elif user_choice.upper() == "R" and cpu_choice == "P":
            print("CPU wins")

        elif user_choice.upper() == "R" and cpu_choice == "S":
            print("Player Wins")

        elif user_choice.upper() == "P" and cpu_choice == "R":
            print("Player Wins")

        elif user_choice.upper() == "S" and cpu_choice == "R":
            print("CPU wins")

        elif user_choice.upper() == "S" and cpu_choice == "P":
            print("Player wins")

        elif user_choice.upper() == "P" and cpu_choice == "S":
            print("CPU wins")

start()
