from abc import ABC, abstractmethod

# Creating an interface class, it can not be instantiated

class Iperson(ABC):
    
    # Abstract method which is to be implemented in the child class
    @abstractmethod
    def person_method(self):
        pass


# A person can be a student or the Teacher that's why we have an Interface Person
class Student(Iperson):
    def __init__(self):
        self.name = "Student Name"
        
    def person_method(self):
        print('Hey I am the instance of the Student class')
        
class Teacher(Iperson):
    def __init__(self):
        self.name = "Teacher Name"
        
    def person_method(self):
        print('Hey I am the instance of the Teacher class')
    
# Here we can create the instances of student class manually     
student = Student()
student.person_method()

teacher = Teacher()
teacher.person_method()

# However we will write a factory method which will dynamically create instance of the required class based upon the input

class PersonFactory:
    
    def build_person(self, type_person):
        if type_person == 'Student':
            return Student()
            
        elif type_person == 'Teacher':
            return Teacher()
            
        else: 
            raise Exception('The input is not a valid input type')

factory = PersonFactory()
teacher = factory.build_person('Teacher')
teacher.person_method()
student = factory.build_person('Student')
student.person_method()
