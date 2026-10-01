def hello():
  print("hello")
  

# hello()

def hello2(esm):
  print(f"hello {esm}")
  

# hello2("ali")

def hello3(esm = "user"):
  print(f"hello {esm}")


# hello3()
# hello3("admin")

def hello4(first_name, last_name = ""):
  print(f"hello {first_name} {last_name}")

# hello4("ali")

def hello5(first_name, last_name = "", age = ""):
  print(f"hello {first_name} {last_name} {age}")

# hello5("ali")


def hello6(first_name, last_name = "", age = ""):
  print(f"hello {first_name} {last_name} {age}")

# hello6("ali", age=10)


def hello6(first_name, last_name, age, father_name):
  print(f"hello {first_name} {last_name} age: {age} father: {father_name}")

# hello6(first_name="ali", last_name="", age="", father_name="reza")

def hello7(*args):
  for item in args:
    print(item)

# hello7(10, 20, "ali", "hatami", 50)

def hello8(first_name, *args):
  for item in args:
    print(item)


def hello9(*args, first_name):
  for item in args:
    print(item)

  print(f"first_name: {first_name}")

# hello9("ali", "hatai", first_name="reza")

def hello10(first_name, last_name, *, age):
  print(f"first_name: {first_name}")

# hello10("ali", "rezaei", age=10)

def hello11(**kwargs):
  #for item in kwargs:
  #  print(item)
  # print(kwargs)
  print(kwargs["age"])

# hello11(name="reza", family="hatami", age=50, list1=[10,20,30])

def hello12(request, *args, **kwargs):
  print(request)
  print(args)
  print(kwargs)

hello12("test", 10, 20, age=50)