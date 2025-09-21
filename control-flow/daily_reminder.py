task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
timeBound = input("Is it time-bound? (yes/no): ")

match priority.lower():
    case "high":
        if timeBound.lower() == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        elif timeBound.lower() == "no":
            print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
    case "medium":
        if timeBound.lower() == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        elif timeBound.lower() == "no":
            print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
    case "low":
        if timeBound.lower() == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        elif timeBound.lower() == "no":
            print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
    case _:
        print("Wrong priority selected")

