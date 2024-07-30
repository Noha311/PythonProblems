#--------------------------Decorator-----------------------------
from time import time
def speedTest(fun):
    def nestedfun():
        start = time()
        fun()
        end = time()
        print(f"Function Speed Time Is: {end - start}")
    return nestedfun
@speedTest
def myFun():
    for num in range(1,40000):
        print(num)
myFun()