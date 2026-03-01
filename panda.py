class Panda:
    def __init__(self, name, age, weight, color):
        self.name = name
        self.age = age
        self.weight = weight
        self.color = color

    def eat(self):
        print(self.name, "is eating")

    def sleep(self):
        print(self.name, "is sleeping")