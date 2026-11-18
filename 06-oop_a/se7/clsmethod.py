class A:
  def __init__(self, name, family):
    self.name = name
    self.family = family

  @classmethod
  def create_a(cls, f, n):
    return cls(n, f)

a = A.create_a("ali", "rezaei")
print(a.family)
print(a.name)