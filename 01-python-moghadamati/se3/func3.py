def hello(name, family="", * , temp):
  print(f"salam {name} {family} khoobi")
  if temp is not None:
    print("temp", temp)
  

hello("ali", temp=10)
