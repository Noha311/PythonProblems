from termcolor import colored

print(colored("="*30 + " WELCOME TO OUR PYTHON JOURNEY " + "="*24, 'magenta'))

print("-" * 60)
print("Fname    Lname     Age    Country")
print("Noha     Elsayed   21     Egypt")
print("-" * 60)

key_word = ["Fname", "Lname", "Age", "Country"]
value = ["Noha", "Elsayed", 21, "Egypt"]

dict_value = dict(zip(key_word, value))

for item in dict_value:
    print(f"{item} : {dict_value[item]}")

print("Please enter 1 if you want to update anything.")
option = int(input("Please Enter Your Option: "))

if option == 1:
    old_val = input("Please enter the field you want to update (Fname, Lname, Age, Country): ")
    if old_val in dict_value:
        new_val = input("Please enter new value: ")
        dict_value[old_val] = new_val
        print("Updated successfully.")
        print("Enter 'y' to confirm or 'n' to exit")
        option2 = input("Please Enter Your Option: ")
        if option2.lower() == 'y':
            for item in dict_value:
                print(f"{item} : {dict_value[item]}")
        elif option2.lower() == 'n':
            print("Thank you.")
        else:
            print("Invalid Choice. Please enter a valid option (y, or n).")
    else:
        print("Invalid field. Please enter a valid field.")
else:
    print("Invalid Choice. Please enter a valid option (1).")
