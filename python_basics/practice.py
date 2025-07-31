class Student:
    def __init__(self , name = "" , roll_number = 0, marks = 0):
        self.name = name
        self.roll_number = roll_number
        self.__marks = marks
    def set_marks(self,marks):
        mark1 = int(input("Enter the input 1 :"))
        mark2 = int(input("Enter the input 2 :"))
        mark3 = int(input("Enter the input 3 :"))
        mark4 = int(input("Enter the input 4 :"))
        mark5 = int(input("Enter the input 5 :"))
        self.marks = mark1+mark2+mark3+mark4+mark5
        return marks
    def get_marks(self , marks):
     self.marks=marks
     print(marks)
s = Student()
s.set_marks(22)
s.get_marks()
        