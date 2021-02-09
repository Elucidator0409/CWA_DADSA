class Product:
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity
    def createCopy(self):
        return Product(self.item.createCopy(), self.quantity)
    def __eq__(self, other):
        return self.item.name == other.item.name