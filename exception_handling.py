file_Name = None
num_of_tries = 3
while num_of_tries > 0:
      try:
       print("Enter The File Name With Absolute Path To Open")

       print(f"You Have {num_of_tries} Tries Left")

       print("Example: D:\Python\Files\yourfile.extension")

       file_name_and_path = input("File Name => : ").strip()

       the_file = open(file_name_and_path, 'r')

       print(the_file.read())

       break 
      except FileNotFoundError:
        print("File Not Found Please Be Sure The Name is Valid")

        num_of_tries -= 1

      except:

        print("Error Happen")

      finally:
          if file_Name != None:
             file_Name.close()
             print("closed Is Done")

else:
   print("All Tries Is Done")




