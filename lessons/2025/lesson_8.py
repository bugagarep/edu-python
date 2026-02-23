class Animal:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def speak(self):
        return "Some animal is saying something..."

    def info(self):
        return f"{self._name}, {self._age} years old"

class Dog(Animal):
    def speak(self):
        return f"Woof-woof! I'm {self._name}!"

class Cat(Animal):
    def speak(self):
        return "Meow-meow!"

class Lion(Animal):
    def speak(self):
        return "Grrrrr!"

animals = [
    Dog("Charlie", 3),
    Cat("Luna", 2),
    Lion("Simba", 5)
]

for animal in animals:
    print(animal.info(), "is saying -", animal.speak())
############################################################################
class Human:
    def __init__(self, name, age):
        self._name = name
        self._age = age

class Student(Human):
    def __init__(self, name, age, grade, subjects, average_score):
        super().__init__(name, age)
        self._grade = grade
        self._subjects = subjects
        self._average_score = average_score
