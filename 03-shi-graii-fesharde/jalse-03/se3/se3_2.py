class MobileMixin:
  def func1(self):
     print("fuunnnnn1")


class SmartPhone:
   def __init__(self, os):
      self.os = os
      self.color = "reeeeeed"


class Machin(SmartPhone, MobileMixin):
   pass

obj1 = Machin("android")
print(obj1.color)
obj1.func1()
