#single inheritance
class Person:
    def say_hello(self):
        print("Hello!")
class Student(Person):
    def study(self):
        print("studying...")
myobj = Student()
myobj.say_hello()
myobj.study()

#Multilevel inheritance 
class Device():
    def power_on(self):
        print("This is power_on()")
class Computer(Device):
    def boot_os(self):
        print("This is boot os")
class Laptop(Computer):
    def open_lid(self):
        print("This is open_lid()")

obj = Laptop()
obj.power_on()
obj.boot_os()
obj.open_lid()

#heirarichical inheritance 

class Shape:
    def area(self,length=0 , breadth=0 ,radius=0):
        self.length = length
        self.breadth = breadth
        self.radius = radius
class Rectangle(Shape):
    def area(self ,length , breadth  ):
       self.length=length
       self.breadth=breadth
       area = self.length+self.breadth
       print(f"Area of rectangle : {area}")
class Circle(Shape):
    def area(self,radius):
        self.radius=radius
        area = self.radius*self.radius*3.1416
        print(f"Area of Circle : {area}")
r = Rectangle()
r.area(20,56)
c = Circle()
c.area(2)

#multiple inheritance 
class Writter:
    def write(self):
        print("This is write()")
class Artist:
    def draw(self):
        print("this is draw()")
class Designer(Writter , Artist):
    def create_design(self):
        print("Designing complete")
        
Designer = Designer()
Designer.write()
Designer.draw()
Designer.create_design()

#hybrid inheritance 
class Person:
    def info(self):
        print("I am a Person")
class Teacher(Person):
    def teach(self):
        print("This is teach()")
class Student(Person):
    def learn(self):
        print("This is learn()")
class TeachingAssistant(Teacher , Student):
    def __init__(self):
        super().__init__()
        
tes = TeachingAssistant()
tes.info()
tes.learn()
tes.teach()