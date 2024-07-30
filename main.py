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


