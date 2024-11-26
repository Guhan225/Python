from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class rectangle(shape):
    def __init__(self,width,height):
            self.width=width
            self.height=height
    def area(self):
     return self.width*self.height
rectangle=rectangle(10,5)
print("Rectangle area:",rectangle.area())