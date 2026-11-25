class Mobile:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model 

class SmartPhone(Mobile):
  def __init__(self, brand, model, os):
    super().__init__(brand, model)
    self.os = os
    

smart_mobile = SmartPhone("samsung", "s24", "ANDROID 12")
print(smart_mobile.os)
print(smart_mobile.brand)