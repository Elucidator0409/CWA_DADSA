class Order:
    def __init__(self, name,itemlist , order):
        self.name = name
        self.itemlist = itemlist
        self.order = order
        self.print = print("Order of {0} is : {1} {2}".format(name,itemlist,order))
