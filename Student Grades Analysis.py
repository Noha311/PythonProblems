from functools import reduce

print("="*30 + " WELCOME TO OUR PYTHON JOURNEY " + "="*24)
print("="*30 + " HELLO TO MY 'Student Grades Analysis' " + "="*16)
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
        print("|" + "  1. Enter '1' if you want to retrieve student grade".ljust(79) + " |")
        print("|" + "  2. Enter '2' if you want to delete student data ".ljust(79) + " |")
        print("|" + "  3. Enter '3' if you want to append student grade".ljust(79) + " |")
        print("|" + "  4. Enter '4' if you want to modify student grade ".ljust(79) + " |")
        print("|" + "  5. Enter '5' if you want to search student grade ".ljust(79) + " |")
        print("|" + " "*80 + "|")
        print("-"*80)
        
        option = int(input("Please Enter Your Option: "))

        with open(r"C:\Users\Alshuruq Company\Desktop\PythonProblems\StudentGrade.txt", 'r') as myfile:
            student_data = myfile.readlines()
        
        if option == 1:
            print(f"Our Student details: {''.join(student_data)}")
        
        elif option == 2:
            student_name_to_delete = input("Enter the student name to delete: ")
            updated_data = list(filter(lambda line: student_name_to_delete not in line, student_data))
            with open(r"C:\Users\Alshuruq Company\Desktop\PythonProblems\StudentGrade.txt", 'w') as myfile:
                myfile.writelines(updated_data)
            print(f"Data for {student_name_to_delete} has been deleted successfully.")
        
        elif option == 3:
            new_data = input("Enter the data you want to append (ID,Name,Grade): ")
            with open(r"C:\Users\Alshuruq Company\Desktop\PythonProblems\StudentGrade.txt", 'a') as myfile:
                myfile.write(new_data + "\n")
            print("Data appended successfully.")
        
        elif option == 4:
            modify_data = input("Enter the data you want to modify (name and all line detail): ")
            new_data = input("Enter the new data to replace the old data: ")
            updated_data = list(map(lambda line: new_data + "\n" if modify_data in line else line, student_data))
            found = reduce(lambda acc, line: acc or (modify_data in line), student_data, False)
            if found:
                with open(r"C:\Users\Alshuruq Company\Desktop\PythonProblems\StudentGrade.txt", 'w') as myfile:
                    myfile.writelines(updated_data)
                print("Data modified successfully.")
            else:
                print("Sorry, the specified data was not found.")
        
        elif option == 5:
            search_data = input("Enter the data you want to search (name and all line detail): ")
            search_results = list(filter(lambda line: search_data in line, student_data))
            if search_results:
                print(f"Student grade: {''.join(search_results)}")
            else:
                print("Sorry, the specified data was not found.")
        
        else:
            print("Invalid choice. Please enter a valid option (1, 2, 3, 4, or 5).")
    
    else:
        print("Incorrect Password.")
else:
    print("Sorry, you are not an admin. You cannot proceed.")
