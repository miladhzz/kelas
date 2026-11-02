class Mobile:  
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
    self._battery = 100

  @property
  def battery(self):
      return self._battery

  @battery.setter
  def battery(self, value):
    if value < 10:
       raise ValueError("Battery muse dsfdsfdsfd...")
    self._battery = value


    
a = Mobile("samsung", "a10")
a.battery = 20
print(a.battery)
