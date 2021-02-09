class House:
    def __init__(self, name,itemNameList , need):
        self.name = name
        self.itemNameList = itemNameList
        self.tempItemList = itemNameList[:]
        self.productList = []
        self.purchasedProductList= []
       
        self.need = need
    
    def createCopy(self):
        newName = self.name
        newProductList = []
        for i in self.productList:
            newProductList.append(i.createCopy())

           
        tempNeed = self.need
        return House(self.tempName, self,productList , self.tempNeed)
        #self.print = print("House of {0} is : {1} {2}".format(name,itemlist,need))
    
    def __eq__(self, other)
        return self.name == other.name