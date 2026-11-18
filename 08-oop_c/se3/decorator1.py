def deco(func):
  print("start")
  func()
  print("end")


@deco
def salam():
  print('salam')


salam()