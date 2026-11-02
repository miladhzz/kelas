class Mobile:  
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
    self._battery = 100

  @staticmethod
  def calc(a, b):
    return a + b

    

print(Mobile.calc(10, 20))

