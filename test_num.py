# import numpy as np
# from numpy import*
# # angle_in_degrees = 30
# # angle_in_radians = np.radians(angle_in_degrees)

# print(np.sin(30*np.pi/180))

import numpy as np
from numpy.core.umath import deg2rad

angle_in_degrees = 30
angle_in_radians = np.radians(angle_in_degrees)

print(np.sin(angle_in_radians))
print(np.cos(angle_in_radians))
print(np.tan(angle_in_radians))

print("="*60)

a = np.sin(deg2rad(30))
b = np.cos(np.deg2rad(30))
c = np.tan(deg2rad(30))
print(a)
print(b)
print(c)
print("="*60)

a = round(3.5)
b = round(3.68528,1)
c = round(3.68528,2)
d = round(3.68528,3)
e = round(3.68528,4)
print(a)
print(b)
print(c)
print(d)
print(e)

print("="*60)

a =np.floor(3.18)
b =np.ceil(3.18)
print(a)
print(b)

print("="*60)

v = (1,2,3)
print(np.array(v))

print("="*60)

a = np.array([range(i, i + 4) for i in [2, 4, 6, 8]])
print(a)

print("="*60)

a = np.array([('x',3,4.2),('y',4,5.3),('z',5,6.3)],
dtype =[('name','U5'),('number','i2'),
('value','f4')])
print(a)
print("=" *60)

import random
print(np.random.uniform(1, 5, 5))  # Output: Random float between 1 and 10
print(np.random.normal(2, 5, 5)) 
print(np.random.random((2, 5))) #2 => rows , 5 => cols
print(np.random.randint(3,10,(3,3,5))) 
print("=" *60)

a = np.full((3, 5), 35)
print(a)
print("=" *60)

a =np.arange(18).reshape(3,6)
print(a)

print("=" *60)

b =np.arange(27).reshape(3,3,3)
print(b)

print("=" *60)
b =np.linspace(0,30)
c =np.linspace(0,100,5)
print(b)
print(c)
print("=" *60)

a =np.diag(np.array([5,12,4,-1,3]))
b =np.diag(np.array([5,12,4,-1,3]),k=3)

print(a)
print(b)

print("=" *60)
a = np.random.randint(0, 10, (3, 3))
b = np.count_nonzero(a)
print(a)
print(b)
print("=" *60)

a = np.random.randint(0, 10, (3, 3))
b = np.count_nonzero(a>5,axis=1)
c = np.count_nonzero(a<8,axis=1)
d = np.any(a>5)
e = np.all(a>5)

print(a)
print(b)
print(c)
print(d)
print(e)
print("=" *60)
a =np.random.randint(5,20, size=9).reshape(3,3)
b = a>10
c = a<15
print(a)
print('-------------------------')
print(b)
print('-------------------------')
print(c)
print("=" *60)
a =np.arange(9).reshape(3,3)
b =np.arange(9).reshape(3,3)
c = 2*b
d = np.isclose(a,b,rtol = 0.1)
e = np.isclose(a,c,rtol = 0.1)
print(a)
print('-------------------------')
print(b)
print('-------------------------')
print(c)
print('-------------------------')
print(d)
print('-------------------------')
print(e)
print("="*60)
a =np.arange(5)
b =np.empty(5)
np.multiply(a, 10, out=b)
print(a)
print(b)
print("="*60)
a =np.arange(5)
b =np.empty(5)
np.power(a, 2, out=b)
print(a)
print(b)
print("="*60)
a =np.arange(15)
b =np.add.reduce(a)
print(a)
print(b)
print("="*60)
a =np.arange(1,15)
b =np.multiply.reduce(a)
print(a)
print(b)
print("="*60)
a =np.arange(2,8)
b =np.multiply.outer(a,a)
print(a)
print(b)
print("="*60)
a =np.arange(15)
b =np.add.accumulate(a)
print(a)
print(b)
print("="*60)
a =np.arange(2,8)
b =np.multiply.accumulate(a)
print(a)
print(b)
print("="*60)
a =np.arange(12)
b = len(a)
c = a.reshape(3,4)
d = len(c)
v = c.size
h=c.ndim
print(a)
print(b)
print(c)
print(d)
print(v)
print(h)
print("="*60)
a =np.array(['a','d','g','h','j'])
b = a.dtype
c = np.arange(12)
d = c.reshape(3,4)
e = d.dtype
print(a)
print(b)
print(c)
print(d)
print(e)
print("="*60)

a =np.arange(9)
b = a.reshape(3,3)
c = np.trace(b)
print(a)
print(b)
print(c)
print("="*60)
a =np.random.randint(5,20, size=9).reshape(3,3)
b =np.random.randint(5,20, size=3).reshape(3,1)
c = a+b
d = a-b
e = a*b
f = a/b
print(a)
print("-------------------------------------------")
print(b)
print("-------------------------------------------")
print(c)
print("-------------------------------------------")
print(d)
print("-------------------------------------------")
print(e)
print("-------------------------------------------")
print(f)


