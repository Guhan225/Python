class person:
    def init(self,name,age):
       self.name=name
       self.age=age
    def greet(self):
        print("Hello, my name is{self.name}and I am {self.age}years old.")
        person1=person("Alice",30)
        person1.greet()
class student_id(person):
    def init(self,name,age,student_ID):
        super().init(name,age)
        self.student_id=student_id
    def display_id(self):
        print("My student ID is {self.student_id}.")
student1=student_id("Bob",20,"S123")
student1.greet()
student1.display_id()