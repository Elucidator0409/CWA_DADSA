class Order:
    def __init__(self, name,itemlist , need):
        self.name = name
        self.itemlist = itemlist
        self.tempItemList = itemlist
        
       
        self.need = need
    def createCopy(self)
        tempName = self.name
        tempItemList =  self.itemlist
        
        tempTempItemList = self.tempItemList
        tempNeed = self.need
        return Order(self.tempName, self,tempItemList, self.tempTempItemList, self.tempNeed)
        #self.print = print("Order of {0} is : {1} {2}".format(name,itemlist,need))
