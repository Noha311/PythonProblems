print("="*30 + " WELCOME TO OUR PYTHON JOURNEY " + "="*24)
print("="*30 + " HELLO TO MY 'AdminFileAccess' " + "="*24)
print("-"*80)
myDataset = ["Noha", "Mahmoud", "Beka", "Omar", "Logain"]
Password_list = ["noha12", "mahmoud33", "beka23", "omar89", "login88"]

username = input("Please Enter Your Username: ")
Password = input("Please Enter Your Password: ")

if username in myDataset:
    pass_index = myDataset.index(username)

    if Password == Password_list[pass_index]:
        print("-"*80)
        print("|" + " "*80 + "|")
        print("|" + " Please Choose The Suitable options: ".ljust(79) + " |")
        print("|" + "  1. Enter '1' if you want to read".ljust(79) + " |")
        print("|" + "  2. Enter '2' if you want to append".ljust(79) + " |")
        print("|" + "  3. Enter '3' if you want to modify".ljust(79) + " |")
        print("|" + " "*80 + "|")
        print("-"*80)
        option = int(input("Please Enter Your Option: "))
        
        if option == 1:
            with open(r"C:\Users\Alshuruq Company\Desktop\PythonProblems\miniFileProject.txt", "r") as myfile:
                student_data = myfile.read()
            print(f"Our Student details: {student_data}")
        
        elif option == 2:
            new_data = input("Enter the data you want to append (name, age, grade): ")
            with open(r"C:\Users\Alshuruq Company\Desktop\PythonProblems\miniFileProject.txt", 'a') as myfile:
                myfile.write(new_data + "\n")
            print("Data appended successfully.")
            option2 = input("Do you want to verify the update? Press 'Y' for Yes or 'N' for No: ")
            if option2.lower() == "y":
                with open(r"C:\Users\Alshuruq Company\Desktop\PythonProblems\miniFileProject.txt", "r") as myfile:
                    student_data = myfile.read()
                print(f"Our Student details: {student_data}")
            elif option2.lower() == "n":
                print("No problem. Have a nice day! ^^")
            else:
                print("Invalid choice. Please enter a valid option (Y or N).")
        
        elif option == 3:
            modify_data = input("Enter the data you want to modify (name and all line detail): ")
            new_data = input("Enter the new data to replace the old data: ")
            with open(r"C:\Users\Alshuruq Company\Desktop\PythonProblems\miniFileProject.txt", "r") as myfile:
                student_details = myfile.readlines()
            found = False
            with open(r"C:\Users\Alshuruq Company\Desktop\PythonProblems\miniFileProject.txt", "w") as myfile:
                for data in student_details:
                    if modify_data in data:
                        myfile.write(new_data + "\n")
                        found = True
                    else:
                        myfile.write(data)
            if found:
                print("Data modified successfully.")
            else:
                print("Sorry, the specified data was not found.")
        
        else:
            print("Invalid choice. Please enter a valid option (1, 2, or 3).")
    else:
        print("Incorrect Password.")
else:
    print("Sorry, you are not an admin. You cannot proceed.")
