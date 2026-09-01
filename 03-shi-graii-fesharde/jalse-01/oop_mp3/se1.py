class Mobile:
  serial_number = 123

  def __init__(self, brand, color, os=None):
    self.brand = brand
    self.color = color
    self.os = os

  def test1(self):
    self.color = "red"
    

mobile1 = Mobile("nokia 1100", "silver")
mobile1.test1()
mobile2 = Mobile("samsung", "silver", "android")
print(mobile1.os)
print(mobile2.os)