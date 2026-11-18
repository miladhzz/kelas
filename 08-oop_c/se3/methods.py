class Mobile:
  os = "ANDROID"

  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
    self.size = "5 inch"    

  def show(self, battery):
    print("salam", battery)

  
mobile = Mobile("LG", "K10")
mobile1 = Mobile("dfsf", "fdsfd")
mobile1.show(50)