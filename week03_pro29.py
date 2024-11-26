class animal:
    def sound(self):
        print("Some generic animals sound")
class dog(animal):
    def sound(self):
        print("Bark")
class cat(animal):
    def sound(self):
        print("Meow")
animals=[animal(),dog(),cat()]
for animal in animals:
    animal.sound()