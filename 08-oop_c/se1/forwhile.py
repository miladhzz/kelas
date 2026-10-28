for i in range(10):
  password = input("pass ???")
  if password == "admin":
    print("welcome")
    break
  elif i == 2:
    print("locked!")
    break


counter = 0
while True:
  password = input("pass ???")
  counter+=1
  if 