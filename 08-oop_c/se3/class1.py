class Mobile:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model


brand = input("Enter Brand: ")
model = input("Enter Model: ")

mobile = Mobile(brand, model)
# print(nokia.__dict__)
print(mobile.model)
print(mobile.brand)
