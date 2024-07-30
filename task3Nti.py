x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

formatted_strings = list(map(lambda label, x, y, z: f"{label}: {x}, {y}, {z}", labels, x_coord, y_coord, z_coord))
print(formatted_strings)
for i in formatted_strings:
    print(i)

print("---------------------------------------------------------------")
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]
formatted_strings = list(map(lambda cast_name, cast_height: f"{cast_name}: {cast_height}", cast_names,cast_heights))
for i in formatted_strings:
    print(i)


print("------------------------------------------------------------")
print("="*30 + " HELLO TO MY 'Mini Calculator' " + "="*24)
print("-"*80)
print("|" + " "*80 + "|")
print("|" + " Please Choose The Suitable options: ".ljust(79) + " |")
print("|" + "  1. Enter '1' if you want to ADD".ljust(79) + " |")
print("|" + "  2. Enter '2' if you want to SUB".ljust(79) + " |")
print("|" + "  3. Enter '3' if you want to MULTI".ljust(79) + " |")
print("|" + "  3. Enter '4' if you want to DIV".ljust(79) + " |")
print("|" + " "*80 + "|")
print("-"*80)
option = int(input("Please Enter Your Option: "))
if option == 1:
    def sum(*num):
        sum = num + num
    nums = int(input("Please Enter Your Nums. "))
if option == 2:
    


        
