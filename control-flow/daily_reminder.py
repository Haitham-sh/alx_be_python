task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match time_bound:
    case "yes":
        kind_of_reminder = "Reminder"
        massage = " that requires immediate attention today!"
    case "no":
        kind_of_reminder = "Note"
        massage = ". Consider completing it when you have free time."
    case _:
        print("Invalid input for time-bound. Please enter 'yes' or 'no'.")


print(f"{kind_of_reminder}: '{task}' is a {priority} priority{massage}")