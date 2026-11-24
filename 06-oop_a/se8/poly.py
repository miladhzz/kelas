class Animal:
  def sound(self):
    raise NotImplementedError("پیاده سازی نکردی")


class Cat(Animal):
  def sound(self):
    print("miooooo")


class Dog(Animal):
  def sound(self):
    print("vagh vagh")


def test(obj):
  obj.sound()


test(Dog())