# Import all workout classes
import cardio, hiit, legs, pull, push, db_access, nutrition
import random
from datetime import datetime
import sqlite3

# Implement Random to choose 3 random workouts from each category
def rand(workoutList, n):
    return random.sample(list(workoutList), n)


# Get time of day to greet the user
def get_time_greeting(user):
    now = datetime.now()
    if now.hour < 12:
        print(f"Good morning {user}")
    elif now.hour >= 12 and now.hour < 17:
        print(f"Good afternoon {user}!")
    else:
        print(f"Good evening {user}!")


# Turn the random list into a string to print out
def list_to_string(list):
    string_value = "For your workout today you will be doing: "
    for i in range(len(list)):
        workouts = ", ".join(list)
    print(string_value + workouts)


# Questionaire Class
def questionaire(self):
    # Initialize database
    self.db = db_access
    
    # Set Loop
    looping = True
    firstName = ""
    lastName = ""

    # Welcome Message
    print("Welcome to Workout Generator!")

    # Login function
    while looping:
        firstName = input("What is your first name: ")
        lastName = input("What is your last name: ")
        if self.db.login(firstName, lastName):
            print("You have successfully logged in!")
            break
        else:
            print(
                "You are not in the database!\n Would you like me to add you to the database? (y/n)"
            )
            add_user_response = input().upper()
            if add_user_response == "Y":
                self.db.add_user(firstName, lastName)
                print("You have been added to the database!")
                break
            else:
                continue
            continue

    # Greet the user
    get_time_greeting(firstName.capitalize())
    print("Let's get started!")
    while looping:
        try:
            type_of_workout = input(
                "What type of workout would you like to do today?\n 1. Cardio\n 2. HITT\n 3. Legs\n 4. Pull\n 5. Push\n Enter the number here > "
            )
            type_of_workout = int(type_of_workout)
            if type_of_workout == 1:
                print("You have chosen cardio!")
                rand_cardio_list = rand(self.cardio.cardio_workouts, 3)
                list_to_string(rand_cardio_list)
                break
            elif type_of_workout == 2:
                print("You have chosen HIIT!")
                rand_hiit_list = rand(self.hiit.hiit_workouts, 3)
                list_to_string(rand_hiit_list)
                break
            elif type_of_workout == 3:
                print("You have chosen legs!")
                rand_legs_list = rand(self.legs.leg_workouts, 3)
                list_to_string(rand_legs_list)
                break
            elif type_of_workout == 4:
                print("You have chosen pull!")
                rand_pull_list = rand(self.pull.pull_workouts, 3)
                list_to_string(rand_pull_list)
                break
            elif type_of_workout == 5:
                print("You have chosen push!")
                rand_push_list = rand(self.push.push_workouts, 3)
                list_to_string(rand_push_list)
                break
        except ValueError:
            print("Please enter a valid number!")


class main:
    def __init__(self):
        # Initialize all workout classes
        self.cardio = cardio.Cardio
        self.hiit = hiit.HIIT
        self.legs = legs.Legs
        self.pull = pull.Pull
        self.push = push.Push

    def main(self):
        questionaire(self)


if __name__ == "__main__":
    workout = main()
    workout.main()
