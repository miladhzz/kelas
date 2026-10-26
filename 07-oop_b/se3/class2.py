class Mobile:  
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def call(self, phone_number):
    print("calling...", phone_number)

class SmartPhone(Mobile):
  def call(self, phone_number):
    print("SMART")
    super().call(phone_number)
    

a = SmartPhone("samsung", "a10")
a.call("09456456")
