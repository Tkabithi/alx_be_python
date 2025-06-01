print("Daily Task Reminder")
task = input("Enter your task: ")
while True:
    priority = input("Priority (high/medium/low): ").lower()
    if priority in ('high', 'medium', 'low'):
        break
    print("Invalid priority. Please enter high, medium, or low.")
while True:
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    if time_bound in ('yes', 'no'):
        break
    print("Please answer yes or no.")
match priority:
    case 'high':
        if time_bound == 'yes':
            reminder = f"'{task}' is a HIGH priority task that requires immediate attention today!"
        else:
            reminder = f"'{task}' is a HIGH priority task that is important but not urgent."
    case 'medium':
        if time_bound == 'yes':
            reminder = f"'{task}' is a MEDIUM priority task that should be completed soon!"
        else:
            reminder = f"'{task}' is a MEDIUM priority task that can be scheduled for this week."
    case 'low':
        if time_bound == 'yes':
            reminder = f"'{task}' is a LOW priority task that needs to be done today."
        else:
            reminder = f"'{task}' is a LOW priority task. Consider completing it when you have free time."


print("\nReminder:", reminder)