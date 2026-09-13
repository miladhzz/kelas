class Mobile:
  serial_number = 123

  def __init__(self, brand, color, os=None):
    self.brand = brand
    self.color = color
    self.os = os

  def test1(self):
    self.color = "red"
    

mobile1 = Mobile("nokia 1100", "silver")

try:
  print(1/0)
  print(mobile1.size)
except AttributeError:
  print("AttributeError")
except:
  pass
else:
  print("okkkkk")

print(mobile1.color)