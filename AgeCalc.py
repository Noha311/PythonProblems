print("="*30 + " WELCOME TO OUR PYTHON JOURNEY " + "="*30)
print("="*30 + " Let's Start Using My Project 'AgeCalc' " + "="*29)
print("-"*80)
print("|" + " "*78 + "|")
print("|" + " Please Choose The Suitable Time Unit: ".ljust(76) + " |")
print("|" + "  1. Enter '1' if you want to calculate age in Days".ljust(76) + " |")
print("|" + "  2. Enter '2' if you want to calculate age in Weeks".ljust(76) + " |")
print("|" + "  3. Enter '3' if you want to calculate age in Months".ljust(76) + " |")
print("|" + " "*78 + "|")
print("-"*80)

# Prompt user for input
Age = int(input("Please Enter Your Age in Years: "))
TimeUnit = int(input("Please Enter The Time Unit You Prefer: "))

# Perform calculations based on user choice
if TimeUnit == 1:
    days = Age * 365  # Calculate age in days 
    print(f"Your Age in Days is: {days}")
elif TimeUnit == 2:
    weeks = Age * 52  # Calculate age in weeks 
    print(f"Your Age in Weeks is: {weeks}")
elif TimeUnit == 3:
    months = Age * 12  # Calculate age in months
    print(f"Your Age in Months is: {months}")
else:
    print("Invalid choice. Please enter a valid option (1, 2, or 3).")
    