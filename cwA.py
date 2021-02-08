import csv

from Store  import Store
from House  import House
from Reader import Reader
from LinkList import Node
from LinkList import  DoublyLinkedList
from Product import Product
from Item import Item




'''
__MAIN__
'''
#create the blank list 
listOfHouse = DoublyLinkedList()
listOfStore = DoublyLinkedList()

#read data from the file
read = Reader(listOfStore, listOfHouse)




listOfItem = []

itemNameList, costList, storeName = read.readItemList()
houseNum = read.readHouseNumList()

for i in range(0, 27):
    tempListOfItem = Item(itemNameList[i], costList[i])
    listOfItem.append(tempListOfItem) 


#create list of product for each house
for i in houseNum:
    tempHouse = listOfHouse.searchNode(i) #search to house
    listOfOrder = tempHouse.need #take house order
    productList = []
    
    tempListOfItem = listOfItem 
    count = 0
    for i in listOfOrder:
  
        if (i == 1 or i == 2):
        
            tempListOfProduct = Product(tempListOfItem[count], i)
            
            count = count +1
            productList.append(tempListOfProduct) 
        else:
            count = count+1  
        tempHouse.productList = productList #add product list to house


#main Algorithm
daysCheck  = 0
daysCount  = 1
bought     = []
buyInDay   = []
needBuy    = []

while daysCount<=7 :
    for a in houseNum:
        House = listOfHouse.searchNode(a) #search
        Order = House.productList    
        for i in storeName:
            Store = listOfStore.searchNode(i) #search
            Store.sortStore()
            for b in Order:
                


'''
def toDO(): 
    itemList, costList, storeName = read.readItemList()
    houseNum = read.readHouseNumList()
    for i in houseNum:
        print(i)
    productList = []
    quantityList = []
    buyList = []
   
    
    #create list of product with name + cost
    for i in range(0, 27):
        tempProduct = Product(itemList[i], costList[i])
        productList.append(tempProduct) # list of product 
  
    
   
    #for y in tempProductList:
        #print(y.name+"    "+ y.cost)
    count = 0

    
    testName=["1A"]   
    
    bought = []
    buyInDay = []
    tempBuyInDay = []
    needBuy = []
    quantityList = []
    daysCount = 0
    canDeli = []
       
    
    for a in testName:
        tempHouse = house.searchNode(a) #search to house
        tempNeed = tempHouse.need
         #take order list from house
        #print("do1")    
        for i in storeName: 
            tempList1 = store.searchNode(i) #search store
            tempList1.sortStore()           #sort item list in store
            tempList2 = tempHouse.itemlist 
            tempList3 = tempHouse.tempItemList
            
            #print("do2")
            for b in tempNeed: #take quantity from order list
                if b>0 :  #if quantity of item is 1 or 2 
                    print("START")
                    itemCheck = tempList2[0] #take  item from list of item from house corresponding with quantity from order list at that position
                    print("Item to search :"+itemCheck)
                    
                    check = tempList1.search(itemCheck) #search item in item list of store
                    
                   
                    if check == True: 
                        tempHouse.tempItemList.remove(itemCheck) #remove item from temp list in house
                        print("do")
                        for i in tempHouse.tempItemList: 
                            print(i)
                        buyInDay.append(itemCheck) #put item into list of product to buy in store 
                         
                elif len(tempList2)>=1:
                    tempList2.pop(0)
           
                    
                
                
                    if daysCount == 1:   # when shopping at 2 shop in 2 days 
                    if not tempOrder.tempItemList : # if items were removed in tempList => all item found and bought => done and delivery
                        bought = buyInDay  + bought
                        itemDeli = bought
                        bought = []
                        daysCount = 0
                        break
                    
                    else:         
                        for z in bought:
                            tempOrder.tempItemList.append(z) #if order is undone , add item from first store into itemlist one more time to search in third store
                        itemCheck = tempOrder.tempItemList[0] #start to check item again in second store
                        check = tempList1.search(itemCheck)
                        if check == True: 
                            tempOrder.tempItemList.remove(itemCheck) #remove item from temp list in house
                            buyInDay.append(check) #put item into list of product to buy in store  
                        bought = buyInDay #save data of item buy in store second
                        buyInDay = []
                 
                         
               
                

                if daysCount ==0 and check == True:
                    bought = buyInDay  + bought  #add item buy each day into list of item bought 
                   
                    buyInDay = []
                print("END ")
                
                
                     
                        
                    
                daysCount = daysCount + 1 
                if not tempHouse.tempItemList : # if items were removed in tempList => all item found and bought => done and delivery
                    itemDeli = bought
                    print("do4")
                    bought = []
                    daysCount = 0
 '''               
            
                
        

      
#toDO()



#tempFinal = tempBill.order
#print(tempFinal)



    
    



    




#ans = input("Enter Item  : ")



#print(result)
#if checkinStore(ans) == True:
#    print("yes")
#storeB.traverse()









    





