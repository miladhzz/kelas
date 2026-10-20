class Mobile:
  def __init__(self, brand, color):
    self.brand = brand
    self.color = color
    self.__battery = 100

class Smart(Mobile):
  def show(self):
    print(self.__battery)
    

a = Smart("Nokia", "Black")
print(a.__dict__)

