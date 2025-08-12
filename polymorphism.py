class Cars:
    def model(self):
        print("Cars Model")
class Person:
    def model(self):
        print("Person customized")
abc = [Cars(), Person()]

for c in abc:
 c.model()
