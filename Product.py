class Product:
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity
    def createCopy(self):
        return Product(self.item.createCopy(), self.quantity)