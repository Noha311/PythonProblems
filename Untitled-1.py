part1 = 7 * 9
part2 = 5 * 7
total = (17*6) - (part1 + part2)
print(total)

print("="*80)
price = "10.990,00"
print(f"Original price string: {price}")

price = price.replace(".", "temp_placeholder")
price = price.replace(",", ".")

price = price.replace("temp_placeholder", ",")

print(f"After swapping: {price}")
print("--------------------------------------------")


#####################################################
mys = "a man a plan canal panama"
newstring = list (mys)
l = len (newstring) 
c=l
i = 0
counter =0
while (i< l/2 ):
    if newstring [i] == newstring[c-1]:
        counter=counter+1
    else:
        break
    i=i+1
    c=c-1
if counter == (l/2):
    print("Plandrom")
else:
     print("not Plandrom")

print("--------------------------------------------")

mystr =input("please enter string:")
mystr2=list(mystr)
print("num is: ",len(mystr2))
nn=mystr.split(" ")
print("num is: ",len(nn))


print("--------------------------------------------")
n = "hi everyone"
print(n[::])