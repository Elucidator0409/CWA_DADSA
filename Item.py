class Item:
    def __init__(self, name, cost):
              
        self.name = name
        self.cost = cost
    
    def createCopy(self):
        return Item(self.name, self.cost)