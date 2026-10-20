class Mobile:
  MODEL = "AAAAAA"
  def __init__(self):
    self.title = "tttttttt"
    self.MODEL = "BBBBB"
    self.model = "nokia"

a = Mobile()

print(a.MODEL)
print(a.__dict__)