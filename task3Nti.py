x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

x = list(zip(x_coord, y_coord, z_coord))
dict(zip(labels,x))

print("---------------------------------------------------------------")
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]
dict(zip(cast_names,cast_heights))


# main.py
import calc  # type: ignore

def get_numbers():
    while True:
        try:
            print("="*30 + " HELLO TO MY 'Mini Calculator' " + "="*24)
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter numeric values.")

while True:
        command = input("Enter command (add, sub, mult, div) or 'st' to stop: ").strip().lower()
        
        if command == 'st':
            print("Exiting the program.")
            break
        
        if command in ['add', 'sub', 'mult', 'div']:
            num1, num2 = get_numbers()
            
            if command == 'add':
                result = calc.add(num1, num2)
            elif command == 'sub':
                result = calc.subtract(num1, num2)
            elif command == 'mult':
                result = calc.multiply(num1, num2)
            elif command == 'div':
                result = calc.divide(num1, num2)
            
            print(f"Result: {result}")
        else:
            print("Invalid command. Please enter 'add', 'sub', 'mult', 'div' or 'st' to stop.")




        
