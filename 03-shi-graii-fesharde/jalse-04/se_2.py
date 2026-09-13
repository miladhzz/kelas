class Mobile:
  def zang(self):
    pass

class OldPhone(Mobile):
  def zang(self):
    print("zzzzzzzzzzzzzzzzzzz")

class NewPhone(Mobile):
  def zang(self):
    print("dinggggdinggggg")

class MMM():
  pass


old = OldPhone()
new = NewPhone()
m = MMM()

def zang(obj1):
  obj1.zang()

zang(old)