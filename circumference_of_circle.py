import math         #import statement
radius=5            #global declaration Section
class Circle():     #class section
    def getArea(self):
        return math.pi*radius*radius
    def getCircumference(self):
        return radius*2*math.pi
    def showadius():        #sub program section
        print("Radius =",radius)
    showadius()             #playground section
c=Circle()
print("Area =",c.getArea()) 
print("Circumference=",c.getCircumference())
