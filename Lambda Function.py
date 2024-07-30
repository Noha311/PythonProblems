print("="*30 + " WELCOME TO OUR PYTHON JOURNEY " + "="*24)
print("="*30 + " HELLO TO MY 'Lambda Function' " + "="*24)
print("-"*80)
name = input("Please Enter Your Name: ")
hello_msg = lambda name : f"Hello {name}. Nice to meet you ^^"
print(hello_msg(name))