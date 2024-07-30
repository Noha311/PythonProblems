#-------------------------------------Generator-----------------------
def fib(num):
    a , b = 0 , 1
    while a < num:
        yield a
        a ,b = b, a + b
# Create a generator object 
x = fib(5) 
  
# Iterating over the generator object using next
print(next(x))  
print(next(x)) 
print(next(x)) 
print(next(x)) 
print(next(x)) 
  
# Iterating over the generator object using for 
# in loop. 
print("Using for in loop") 
for i in fib(5):  
    print(i)
