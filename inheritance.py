class Cars:
    def model(self):
        print("Cars Model")
class Person(Cars):
    def customize(self):
        print("Person customized")

p=Person()
p.customize()
p.model()