class A:
  def show1(self):
      print("aaaaa")

class BMixin:
  def show2(self):
    print("bbbb")

class C(A, BMixin):
  pass

c = C()
c.show1()
c.show2()