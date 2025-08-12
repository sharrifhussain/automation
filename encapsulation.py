# class Student:
#     def __init__(self):
#         self.__name=""   # Private variable
#     def setname(self,name):
#         self.__name=name      # Setter method
#     def getname(self):
#         return self.__name      # Getter method
# var=Student()   # Create object
# var.setname("Student job is QA")     # Set value
# var.getname()
# print(var.getname())     # Get value
class People:
    def __init__(self):
        self.__name = ""
        self.__age = ""

    def setname(self, name):
        self.__name = name

    def getname(self):
        return self.__name

    def setage(self, age):
        self.__age = age

    def getage(self):
        return self.__age
# Object
obj = People()
obj.setname("Shams")    # Function call
obj.setage(30)          # Function call
obj.getname()
print(obj.getname())
print(obj.getage())



