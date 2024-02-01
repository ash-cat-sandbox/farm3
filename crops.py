import itertools

class Crop:
  def __init__(self, name):
    self.name = name
    

    
class Potatoes(Crop):
  id_iter = itertools.count()
  def __init__(self, name, region):
    super().__init__(name)
    self.region = region
    self.water = 0
    self.pests = 0
    self.weeds = 0
    self.fungus = 0
    self.harvest = 0
    self.location = 0
    self.id = next(self.id_iter)


  