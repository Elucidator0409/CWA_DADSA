import csv

from Store  import Store
from House  import House
from Reader import Reader

from Product import Product
from Item import Item
from Solution import Solution




'''
__MAIN__
'''
#read data from the file
read = Reader()
listOfStore, listOfHouseFirstWeek, listOfHouseSecondWeek = read.readData()


itemNameList, costList, storeName = read.readItemList()
TimesToBuyItems = read.readTimeToBuyItems()

houseNum = read.readHouseNumList()


def getNextStore(visitedStoreName):
    tempStoreName = listOfStore[:]
    
    for i in visitedStoreName:
        tempStoreName.remove(i)
    return tempStoreName

def createProductList():
    
    listOfItem = []
    for i in range(0, 27):
        tempListOfItem = Item(itemNameList[i], costList[i])
        listOfItem.append(tempListOfItem) 


    #create list of product for each house 1st week
    for house in listOfHouseFirstWeek:
        
        listOfOrder = house.need #take house order
        productList = []
    
        tempListOfItem = listOfItem 
        count = 0
        for order in listOfOrder:
  
            if (order == 1 or order == 2):
        
                tempListOfProduct = Product(tempListOfItem[count], i)
            
                count = count +1
                productList.append(tempListOfProduct) 
            else:
                count = count + 1  
            house.productList = productList #add product list to house
    
    for house in listOfHouseSecondWeek:
        
        listOfOrder = house.need #take house order
        productList = []
    
        tempListOfItem = listOfItem 
        count = 0
        for order in listOfOrder:
  
            if (order == 1 or order == 2):
        
                tempListOfProduct = Product(tempListOfItem[count], i)
            
                count = count +1
                productList.append(tempListOfProduct) 
            else:
                count = count + 1  
            house.productList = productList #add product list to house
       

    
listOfRemainingOrders = listOfHouseFirstWeek[:]
listOfVisitedStores = []
CurrentSolution = Solution(TimesToBuyItems)
    
    
def reset(listOfRemainingOrders, listOfVisitedStores, CurrentSolution):
    listOfRemainingOrders = listOfHouseFirstWeek[:]
    listOfVisitedStores = []
    CurrentSolution = Solution(TimesToBuyItems)

def compare(BestSolution, CurrentSolution):
    pre = BestSolution.TimesToBuyItems
    best = CurrentSolution.TimesToBuyItems
    tempPre = 0
    tempBest = 0
    for i in range(len(pre)):
        itemInPre = pre[i]
        itemInBest = best[i]
        tempPre = itemInPre[1] + tempPre
        tempBest = itemInBest[1] + tempBest
    if tempPre > tempBest :
        return 1
    else: 
        return 0


houseDeli = []
def recursionAlgo(store, day):
    if(day > 7):
        reset(listOfRemainingOrders, listOfVisitedStores, CurrentSolution)
    elif not listOfRemainingOrders :
        if(compare(BestSolution, CurrentSolution) > 0): 
            BestSolution = CurrentSolution
            reset(listOfRemainingOrders, listOfVisitedStores, CurrentSolution)
    else:
        for i in listOfRemainingOrders:
            tempList = []
            if (day  % 2 == 0):
                tempList = i.purchasedProductList[:]
                i.purchasedProductList = []
                    

            for y in i.tempItemList:
                check = store.search(y)
                if check == True:
                    i.purchasedProductList.append(y)
                    i.tempItemList.remove(y)
                        
                
            if not i.tempItemList: 
                houseDeli.append(i.name)
                listOfRemainingOrders.remove(i)
                CurrentSolution.ProductNeedToBuy[day].append(i.purchasedProductList)
                if day % 2 == 0 :
                    day = day -1
                    CurrentSolution.ProductNeedToBuy[day].append(tempList)
            else:
                i.tempItemList.append(tempList)
                
        CurrentSolution.HouseNeedToDeli.append(houseDeli)
                

        listOfVisitedStores.append(store)
        nextStore = getNextStore(listOfVisitedStores)

        recursionAlgo(nextStore, day + 1)

for i in  listOfStore:
    recursionAlgo(i, 1)


mainAlgo()





    





