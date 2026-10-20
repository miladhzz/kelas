class A:
  BRAND = "Nokia"

  def __init__(self):
    self.title = "oop"
    self.age = 50

  def hide():
    print("hide")

b = A()
b.title = "bbbbbb"
print(A.BRAND)
A.BRAND = "SAM"
print(A.BRAND)
print(b.BRAND)

'''
def show(self, *args, **kwargs):

'''