class Mobile:
  def __init__(self, br, md):
    self.brand = br
    self.model = md

  def zang(self):
    print("zzzzzzzzz")

class Smart(Mobile):
  pass

mobile = Mobile("Nokia","1100")
mobile.zang()