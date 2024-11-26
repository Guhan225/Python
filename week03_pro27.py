class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
person1=person("Bob",20)
person1.greet()
class student_id(person):
    def __init__(self,name,age,student_id):
        super(). __init__(name,age)
        self.student_id=student_id
    def display_id(self):
        print(f"My student ID is {self.student_id}.")
student1=student_id("Bob",20,"S123")
student1.display_id()