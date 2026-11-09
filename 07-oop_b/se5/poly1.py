from abc import ABC, abstractmethod
class Mashin(ABC):  
  @abstractmethod
  def move(self):
      pass

class Tools:
   def chap(self):
      print("fdsfdsfd")

class Car(Mashin):
   def move(self):
      print("Drive")

class Plane(Mashin):
   def move(self):
      print("Fly")



c = Car()
p = Plane()

def show(aaa):
   aaa.move()

show(p)