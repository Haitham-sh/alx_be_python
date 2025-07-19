task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()





match priority:
    case "high":
        kind_of_reminder = "Reminder"
        if time_bound == "yes":
            massage = " that requires immediate attention today!"
        else:
            massage = ". Consider completing it when you have free time."
    case "medium":
        kind_of_reminder = "Reminder"
        if time_bound == "yes":
            massage = " that requires immediate attention today!"
        else:
            massage = ". Consider completing it when you have free time."
    case "low":
        kind_of_reminder = "Note"
        if time_bound == "yes":
            massage = " that requires immediate attention today!"
        else:
            massage = ". Consider completing it when you have free time."
    case _:
        print("Invalid priority. Please enter high, medium, or low.")

print(f"{kind_of_reminder}: '{task}' is a {priority} priority{massage}")