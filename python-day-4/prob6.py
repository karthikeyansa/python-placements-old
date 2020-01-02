import math
class circle:
    def area(self,r):
        self.r=rad
        a=math.pi*rad*rad
        return a
    def perimeter(self,r):
        self.r=rad
        b=math.pi*2*rad
        return b
rad=int(input('enter the radius:'))
p1=circle()
print("radius:",p1.area(rad))
print("perimeter:",p1.perimeter(rad))
