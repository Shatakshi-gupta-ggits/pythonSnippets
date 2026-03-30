
'''
__init__ = initialize the object
self = current object -- instance variable - belong to obj

class var = defined outside def , shareable - comon for all 


'''
class Student:
    def __init__(self, name, marks, attendence):
        self.name = name
        self.marks = marks
        self.attendence = attendence
        
    def calculate_grade(self):
        if self.marks >= 75:
            return "B"
        elif self.marks <= 75:
            return "C"
        else:
            return "C"
        
        
        
s1 = Student("Rohi", 85, 90)
s2 = Student("Karan", 75, 92)
print(s2.marks)
print(s1.name)
