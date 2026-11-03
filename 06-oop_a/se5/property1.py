class Mobile:
  def __init__(self):
    self._battery = 1000

  @property
  def battery(self):
    return self._battery

  @battery.setter
  def battery(self, value):
    if value < 0 or value > 100 :
      raise ValueError("invalid battery value")
    self._battery = value

a = Mobile()
a.battery = 95
print(a.battery)