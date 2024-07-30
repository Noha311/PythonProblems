class car:
    def __init__(self,color) :
        self.color = color
volvo =car("white")
nisssan =car("red")
print(volvo.color)
print(nisssan.color)
print("="*60)
class calc:
    def __init__(self,p1,p2) :
        self.power2=p1**2
        self.power3=p1**3
a=calc(3,3)
print(a.power2)
print(a.power3)