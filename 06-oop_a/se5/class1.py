class Mobile:
  def __init__(self):
    self.age = 16
    self.__battery = 100
    self._age = 1000

  def get_battery(self):
    print(self.__battery)

class Smart(Mobile):
  def show(self):
    print(self._age)

a = Smart()
