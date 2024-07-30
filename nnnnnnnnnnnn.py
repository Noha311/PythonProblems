from numpy import*
a=[[1,2],[3,4]]
b=array(a)
print (a)
print (b)

print("="*60)
a=array([range(i,i+3) for i in [2,4,6]])
print (a)
b=count_nonzero(a>9)
print("="*60)
print(b)


from numpy import *
a = array([('x',3,4.2),('y',4,5.3),('z',5,6.3)],
dtype =[('name','U5'),('number','i2'),('value','f4')])
print(a)
print(empty((3,2)))
