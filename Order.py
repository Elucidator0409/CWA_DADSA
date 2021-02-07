class Order:
    def __init__(self, name,itemlist , need):
        self.name = name
        self.itemlist = itemlist
        self.tempItemList = itemlist
        
        self.quantityList  = []
        self.need = need
        #self.print = print("Order of {0} is : {1} {2}".format(name,itemlist,need))
