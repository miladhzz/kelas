from abc import ABC, abstractmethod

class Animal(ABC):
  @abstractmethod
  def sound(self):
    pass


class Cat(Animal):
  def sound(self):
    print("miooooo")


class Dog(Animal):
  def sound(self):
    print("vagh vagh")


def test(obj):
  obj.sound()


test(Cat())