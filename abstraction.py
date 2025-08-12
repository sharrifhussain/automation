from abc import abstractmethod

class Animal:
    @abstractmethod   # This method must be implemented in all child classes
    def make_sound(self):
        pass
class Dog(Animal):  # Dog class inherits from Animal and provides its own implementation of make_sound
    def make_sound(self):
        print("Dog says hello")
class Cat(Animal):   # Cat class inherits from Animal and provides its own implementation of make_sound
    def make_sound(self):
        print("Cat says hello")

dog = Dog()   # Creating a Dog object and calling its make_sound method
dog.make_sound()

cat = Cat()   # Creating a Cat object and calling its make_sound method
cat.make_sound()