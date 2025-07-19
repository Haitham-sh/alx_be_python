task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        
        if time_bound == "yes":
            reminder = "Reminder"
            message = " that requires immediate attention today!"
        elif time_bound == "no":
            reminder = "Note"
            message = ". Consider completing it when you have free time."
        else:
            message = ". Please specify if it is time-bound or not."
        print(f"{reminder}: '{task}' is a {priority} priority{message}")
    case "medium":
        
        if time_bound == "yes":
            reminder = "Reminder"
            message = " that requires immediate attention today!"
        elif time_bound == "no":
            reminder = "Note"
            message = ". Consider completing it when you have free time."
        else:
            message = ". Please specify if it is time-bound or not."
        print(f"{reminder}: '{task}' is a {priority} priority{message}")
    case "low":
        
        if time_bound == "yes":
            reminder = "Reminder"
            message = " that requires immediate attention today!"
        elif time_bound == "no":
            reminder = "Note"
            message = ". Consider completing it when you have free time."
        else:
            message = ". Please specify if it is time-bound or not."
        print(f"{reminder}: '{task}' is a {priority} priority{message}")
    case _:
        print("Invalid priority. Please enter high, medium, or low.")
        