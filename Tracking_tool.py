habits = []

#Asking User for how many habits they want to track
num_of_habits = int(input("How many habits would you like to track?"))

#Name of the habits
def name_of_habits(num_of_habits):
    for i in range(num_of_habits):
        habit_name = input("Habit Name:")
        habits[habit_name] = 0

#Asking user if they completed the habit
def habits():
    tracker = 0
    for habit in habits:
        q = input(f"Did you complete {habits}? (yes/no)")
        if q == yes:
            tracker += 1
    else:
        print("You should complete your habit for today!")

#


name_of_habits(num_of_habits)
habits()

