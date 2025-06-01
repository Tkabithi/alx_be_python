# daily_reminder.py

print("Daily Task Reminder")
print("=" * 20)

# Get task from user
task = input("Enter your task: ")

# Get priority with validation
while True:
    priority = input("Priority (high/medium/low): ").lower()
    if priority in ('high', 'medium', 'low'):
        break
    print("Invalid priority. Please enter high, medium, or low.")

# Get time-bound status with validation
while True:
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    if time_bound in ('yes', 'no'):
        break
    print("Please answer yes or no.")

# Generate customized reminder
match priority:
    case 'high':
        if time_bound == 'yes':
            reminder = f"URGENT! Drop everything else - '{task}' must be completed today. This is your top priority!"
        else:
            reminder = f"Important: '{task}' should be your main focus when possible. While not urgent today, don't let it slip!"
    case 'medium':
        if time_bound == 'yes':
            reminder = f"Time-sensitive: '{task}' needs your attention within the next couple days. Schedule time for it soon."
        else:
            reminder = f"'{task}' is worth doing when you have a spare moment. Aim to complete it this week if possible."
    case 'low':
        if time_bound == 'yes':
            reminder = f"Gentle reminder: '{task}' would be good to complete today if you have extra time."
        else:
            reminder = f"Whenever you need a break from more important work, consider doing: '{task}'. No rush though."

# Print the customized reminder
print("\n=== YOUR PERSONALIZED REMINDER ===")
print(reminder)
print("=" * 30)
print("You've got this! 💪")  # Keeping one motivational emoji