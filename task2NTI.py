#First Question
words = ["apple", "banana", "cherry", "date", "elderberry" , "ball"]
letter = 'b'
wanted_list =[]
for word in words:
    if word[0] == letter:
          wanted_list.append(word)
print("output: ",wanted_list)
print("-------------------------------------------------")
#another answer
wanted =list(filter(lambda word : word[0] == letter ,words))
print("output: ",wanted)
print("-------------------------------------------------")
words = ["apple", "banana", "cherry", "date", "fig"]
length = 6

def count_len(text):
    return len(text)

lengths = list(map(count_len, words))
matching_len = [word for word in words if len(word) == length]

print(matching_len)  
print("-------------------------------------------------")

list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list(map(lambda x, y: x * y, list1, list2))
print("my list after multiplying : ",result)

# print("-----------------------------------------------------")
strings = ["apple", " ", "banana", " ", "cherry"]

filtered_strings = list(filter(lambda w: w != " ", strings))
print("my list after removing spaces : ",filtered_strings)
        
