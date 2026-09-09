class Mobile:
  serial_number = 123

  def __init__(self, brand, color):
    self.brand = brand
    self.color = color
    self.__battery = 100
    self._aaa = 50

  def test1(self):    
    print("testtttt1")

  def __str__(self):
   return f'str Mobile brand: {self.brand}, color: {self.color}'

  def __repr__(self):
    return f'repr Mobile brand: {self.brand}, color: {self.color}'

    
class SmartPhone(Mobile):
  def __init__(self, brand, color, os):
    super().__init__(brand, color)    
    self.os = os

  def test_protected(self):
    print(self._aaa)


mobile1 = Mobile("samsung", "red")
print(mobile1)