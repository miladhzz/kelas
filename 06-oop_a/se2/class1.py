class Mobile:
  brand = "BBBB"

  def __init__(self, *args, **kwargs):
    self.size = ""
    self.model = ""


mobile1 = Mobile()
print(mobile1.size)
print(mobile1.model)
print(Mobile.brand)
print(Mobile.size)