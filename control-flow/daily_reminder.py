# daily_reminder.py

# Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match Case statement for priority levels
match priority:
    case "high":
        reminder = f"'{task}' is a high-priority task"
    case "medium":
        reminder = f"'{task}' is a medium-priority task"
    case "low":
        reminder = f"'{task}' is a low-priority task"
    case _:
        reminder = f"'{task}' has an undefined priority"

# Check if the task is time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Print the customized reminder
print(f"Reminder: {reminder}")
