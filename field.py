import itertools

class Field:
    id_iter = itertools.count()
    def __init__(self, location):
        self.location = next(self.id_iter)
        