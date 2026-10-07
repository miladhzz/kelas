def show(nam, *args, **kwrgs):
  print(nam)
  for item in args:
    print(item)
  print(kwrgs["family"])

show("ali",50, 60, name=50, family="hatami", numbers={"abc":"def"})