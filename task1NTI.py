#First Question
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
modified_list =[]
for name in names:
    modified_name = name.replace(" ", "_")
    modified_list.append(modified_name)
print("UnModified list:", names)
print("Modified list:", modified_list)

print("---------------------------------------------------------")

#Second Question
check_prime = [26, 39, 51, 53, 57, 79, 85]
for num in check_prime:
   if num > 1:
    for i in range(2, (num//2)+1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
#Third Question 
print("---------------------------------------------------------")
largest_num = [1, 7, 9, 8, 5]
largest = largest_num[0]

for num in largest_num:
    if num > largest:
        largest = num

print(f"The largest number is {largest}")

print("---------------------------------------------------------")

#Fourth Question
duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
un_dublicated = []
for num in duplicate:
    if num not in un_dublicated:
        un_dublicated.append(num)

print("My List after removing duplicates:", un_dublicated)

print("---------------------------------------------------------")
#Fifth Question
nums = [10, 20, 30, 40, 50, 60]
lsts = [22, 42]
found = False
for i in nums:
    for j in lsts:
        if i == j:
            found = True
            break
        else:
            found = False
if found:
    print("Two Lists have common value")
else:
    print("Two Lists not have common value")

        
