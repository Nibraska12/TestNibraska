from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class Lion(Cat):
    def speak(self):
        return "Roar!"


class GoldenRetriever(Dog):
    def speak(self):
        return "Woof woof!"


dog = Dog("Fido")
cat = Cat("Whiskers")
lion = Lion("Simba")
golden_retriever = GoldenRetriever("Max")

a = 2
