class House:
    def __init__(self, name,itemlist , need):
        self.name = name
        self.itemlist = itemlist
        self.tempItemList = itemlist
        self.productList = []
       
        self.need = need
    '''
    def createCopy()
        tempName = self.name
        tempItemList =  self.itemlist
        
        tempTempItemList = self.tempItemList
        tempNeed = self.need
        return House(self.tempName, self,tempItemList, self.tempTempItemList, self.tempNeed)
        #self.print = print("House of {0} is : {1} {2}".format(name,itemlist,need))
'''