import cardio, hiit, legs, pull, push
import random


def rand(workoutList, n):
    return random.sample(list(workoutList), n)


class main:
    def __init__(self):
        self.cardio = cardio.Cardio
        self.hiit = hiit.HIIT
        self.legs = legs.Legs
        self.pull = pull.Pull
        self.push = push.Push

    def main(self):
        looping = True
        print("Welcome to Workout Generator!")
        firstName = input("What is your first name: ")
        print(f"\nHello {firstName.capitalize()}! Let's get started!")
        while looping:
            try:
                type_of_workout = input(
                    "What type of workout would you like to do today?\n 1. Cardio\n 2. HITT\n 3. Legs\n 4. Pull\n 5. Push\n"
                )
                type_of_workout = int(type_of_workout)
                if type_of_workout == 1:
                    print("You have chosen cardio!")
                    print("Here is a list of cardio workouts: ")
                    print(rand(self.cardio.cardio_workouts, 3))
                    break
                elif type_of_workout == 2:
                    print("You have chosen HIIT!")
                    print("Here is a list of HIIT workouts: ")
                    print(rand(self.hiit.hiit_workouts, 3))
                    break
                elif type_of_workout == 3:
                    print("You have chosen legs!")
                    print("Here is a list of leg workouts: ")
                    print(rand(self.legs.leg_workouts, 3))
                    break
                elif type_of_workout == 4:
                    print("You have chosen pull!")
                    print("Here is a list of pull workouts: ")
                    print(rand(self.pull.pull_workouts, 3))
                    break
                elif type_of_workout == 5:
                    print("You have chosen push!")
                    print("Here is a list of push workouts: ")
                    print(rand(self.push.push_workouts, 3))
                    break
            except ValueError:
                print("Please enter a valid number!")


if __name__ == "__main__":
    workout = main()
    workout.main()
