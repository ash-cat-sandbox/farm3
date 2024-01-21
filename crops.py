

class Crop:
  def __init__(self, name):
    self.name = name
    

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)
    
class Potatoes(Crop):
  def __init__(self, name, region):
    super().__init__(name)
    self.region = region
  