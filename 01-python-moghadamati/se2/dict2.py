list1 = []
for i in range(2):
  dict1 = {
    "name": input("enter your name"),
    "family":  input("enter your family"),
    "age":  int(input("enter your age"))
  }

  list1.append(dict1)


for item in list1:
  print(item)
