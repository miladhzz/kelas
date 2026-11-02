class Mobile:  
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
    self._battery = 100

class ToolsMixin:
  def func1(self):
    print("shopppppp")

class Smart(Mobile, ToolsMixin):
  pass

    
a = Smart("samsung", "a10")
a.func1()

