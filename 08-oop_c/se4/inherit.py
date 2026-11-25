class Mobile:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model 

  def zang(self):
    print("zzzzzzz")

class SmartPhone(Mobile):

  def zang(self):
    print("zzzzzzz ali callling...")

  def aks(self):
    print("akkkkks")



smart_mobile = SmartPhone("samsung", "s24", "ANDROID 12")
print(smart_mobile.brand)
print(smart_mobile.os)
smart_mobile.zang()
smart_mobile.aks()