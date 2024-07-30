print("="*30 + " WELCOME TO OUR PYTHON JOURNEY " + "="*24)
print("="*30 + " HELLO TO MY 'LOGIN PAGE' " + "="*29)
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
        print("|" + "  1. Enter '1' if you want to delete".ljust(79) + " |")
        print("|" + "  2. Enter '2' if you want to modify ".ljust(79) + " |")
        print("|" + " "*80 + "|")
        print("-"*80)
        option = int(input("Please Enter Your Option: "))

        if option == 1:
            myDataset.remove(username)
            Password_list.pop(pass_index)
            print(myDataset)
            print("Deletion is Done.")
        elif option == 2:
            print("-"*80)
            print("|" + " "*80 + "|")
            print("|" + " Please Choose The Suitable options: ".ljust(79) + " |")
            print("|" + "  1. Enter '1' if you want to modify username".ljust(79) + " |")
            print("|" + "  2. Enter '2' if you want to modify password ".ljust(79) + " |")
            print("|" + " "*80 + "|")
            print("-"*80)
            option2 = int(input("Please Enter Your Option: "))

            if option2 == 1:
                new_user = input("Please Enter Your New Username: ")
                myDataset[pass_index] = new_user
                print("Username modification is Done.")
            elif option2 == 2:
                new_pass = input("Please Enter Your New Password: ")
                Password_list[pass_index] = new_pass
                print("Password modification is Done.")
            else:
                print("Invalid Choice. Please enter a valid option (1, or 2).")
        else:
            print("Invalid Choice. Please enter a valid option (1, or 2).")
    else:
        print("Incorrect Password or Username.")
else:
    print("Sorry, you are not an admin.")
    print("-"*80)
    print("|" + " "*80 + "|")
    print("|" + " Are you want to registeration? : ".ljust(79) + " |")
    print("|" + "  1. Enter '1' if you want to register".ljust(79) + " |")
    print("|" + "  2. Enter '2' if you want to not register ".ljust(79) + " |")
    print("|" + " "*80 + "|")
    print("-"*80)
    option3 = int(input("Please Enter Your Option: "))
    if option3 == 1:
      name=input("Please Enter Your Username: ")
      pass_in=input("Please Enter Your Password: ")
      myDataset.append(name)
      Password_list.append(pass_in)
      print("Registeration is done. ")
    elif option3 == 2:
      print("No Problem, Have a nice day ^^ ")
    else:
      print("Invalid Choice. Please enter a valid option (1, or 2).")
 
