# Import all workout classes
import cardio, hiit, legs, pull, push, db_access, nutrition
import random
from datetime import datetime
import api_access as api
import os, sys
import sqlite3

# Initialize classes
cardio = cardio.Cardio
hiit = hiit.HIIT
legs = legs.Legs
pull = pull.Pull
push = push.Push    
    
# Implement Random to choose 3 random workouts from each category
def rand(workoutList, n):
    return random.sample(list(workoutList), n)


# Get time of day to greet the user
def get_time_greeting(user):
    now = datetime.now()
    if now.hour < 12:
        print(f"Good morning {user}!")
    elif now.hour >= 12 and now.hour < 17:
        print(f"Good afternoon {user}!")
    else:
        print(f"Good evening {user}!")


# Turn the random list into a string to print out
def list_to_string(list):
    string_value = "For your workout today you will be doing: "
    for i in range(len(list)):
        workouts = ", ".join(list)
    print(string_value + workouts.lower())


# Options to select from at beginning of program
def options(firstName):
    get_time_greeting(firstName)
    print("What would you like to do?")
    option = int(
        input("1. Request Workouts\n2. Log Workouts\n3. Log Nutrition\n4. Exit\n")
    )
    if option == 1:
        first_option(firstName)
    if option == 2:
        pass
    if option == 3:
        pass
    if option == 4:
        sys.exit()

# Login or add user to database
def login_or_add(firstName):
    # Initialize database
    db = db_access

    # Set loop
    looping = True

    # Welcome Message
    print("Welcome to Workout Generator!")

    # Login function
    while looping:
        firstName = input("What is your first name: ")
        lastName = input("What is your last name: ")
        if db.login(firstName, lastName):
            print("You have successfully logged in!")
            break
        else:
            print("You are not in the database!\n Would you like me to add you? (y/n)")
            add_user_response = input().upper()
            if add_user_response == "Y":
                db.add_user(firstName, lastName)
                print("You have been added to the database!")
                break
            else:
                continue
            continue
    return firstName

# First option to select from
def first_option(firstName):
    # Create loop
    looping = True
    print("Let's get started!")
    while looping:
        try:
            type_of_workout = input(
                "What type of workout would you like to do today?\n 1. Cardio\n 2. HITT\n 3. Legs\n 4. Pull\n 5. Push\n Enter the number here > "
            )
            type_of_workout = int(type_of_workout)
            if type_of_workout == 1:
                print("You have chosen cardio!")
                rand_cardio_list = rand(cardio.cardio_workouts, 3)
                list_to_string(rand_cardio_list)
                break
            elif type_of_workout == 2:
                print("You have chosen HIIT!")
                rand_hiit_list = rand(hiit.hiit_workouts, 3)
                list_to_string(rand_hiit_list)
                break
            elif type_of_workout == 3:
                print("You have chosen legs!")
                rand_legs_list = rand(legs.leg_workouts, 3)
                list_to_string(rand_legs_list)
                break
            elif type_of_workout == 4:
                print("You have chosen pull!")
                rand_pull_list = rand(pull.pull_workouts, 3)
                list_to_string(rand_pull_list)
                break
            elif type_of_workout == 5:
                print("You have chosen push!")
                rand_push_list = rand(push.push_workouts, 3)
                list_to_string(rand_push_list)
                break
        except ValueError:
            print("Please enter a valid number!")

# Second option to select from
def second_option(self, firstname, lastname):
    pass

# Third option to select from
def third_option(self, firstName):
    pass

# Fourth option to select from
def fourth_option(self):
    pass


class main_class:
    def __init__(self):
        pass

    def main_func(self):
        fn = ""
        user = login_or_add(fn)
        options(user)


if __name__ == "__main__":
    workout = main_class()
    workout.main_func()
