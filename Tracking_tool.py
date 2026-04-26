import json
from datetime import date

# ---------- Load Data ----------
def load_data():
    try:
        with open("habits.json", "r") as file:
            return json.load(file)
    except:
        return {}

# ---------- Save Data ----------
def save_data(habits):
    with open("habits.json", "w") as file:
        json.dump(habits, file, indent=4)

# ---------- Add Habits ----------
def add_habits():
    habits = {}
    num = int(input("How many habits would you like to track? "))

    for i in range(num):
        name = input("Habit name: ")
        habits[name] = {
            "streak": 0,
            "last_completed": ""
        }

    return habits

# ---------- Track Habits ----------
def track_habits(habits):
    today = str(date.today())

    for habit in habits:
        tracker = input(f"Did you complete {habit}? (yes/no): ").lower()

        if tracker == "yes":
            # prevent double counting same day
            if habits[habit]["last_completed"] != today:
                habits[habit]["streak"] += 1
                habits[habit]["last_completed"] = today
        else:
            # reset streak if missed
            habits[habit]["streak"] = 0

# ---------- Display ----------
def display_streaks(habits):
    print("\nCurrent Streaks:")
    for habit in habits:
        print(f"{habit}: {habits[habit]['streak']} days")

# ---------- Main Program ----------
def main():
    habits = load_data()

    if not habits:
        habits = add_habits()

    track_habits(habits)
    save_data(habits)
    display_streaks(habits)

# Run program
main()