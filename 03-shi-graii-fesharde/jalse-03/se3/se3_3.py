class Engine:
  def __init__(self, model, hajm, sookht):
     self.model = model
     self.hajm = hajm
     self.sookht = sookht

  def start(self):
     print("start benzini")

class EngineBatghi:
  def __init__(self, model):
     self.model = model

  def start(self):
     print("start batghi")

class Car:
   def __init__(self, model):
      self.model = model
      self.color = "reeeeeed"

class Pride(Car):
   def __init__(self, model, engine):
      super().__init__(model)
      self.engine = engine


enging = EngineBatghi("333")
obj1 = Pride("pride 82", enging)
print(obj1.color)
obj1.engine.start()
