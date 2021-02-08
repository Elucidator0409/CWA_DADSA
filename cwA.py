import csv

from Store  import Store
from Order  import Order
from Reader import Reader
from LinkList import Node
from LinkList import  DoublyLinkedList

from Product import Product




'''
__MAIN__
'''
#create the blank list 
order = DoublyLinkedList()
store = DoublyLinkedList()
#read data from the file
read = Reader(store, order)





def toDO(): 
    itemList, costList, storeName = read.readItemList()
    nameList = read.readNameList()
    productList = []
    quantityList = []
    buyList = []
   
    
    
    for i in range(0, 27):
        tempProduct = Product(itemList[i], costList[i])
        productList.append(tempProduct)
  
    
   
    #for y in tempProductList:
        #print(y.name+"    "+ y.cost)
    count = 0

    
    testName=["1A"]   
    '''
    for a in testName:
        tempOrder = order.searchNode(a)
        tempNeed = tempOrder.need
        tempOrder.tempItemList1 = tempOrder.itemlist
        
        for b in tempNeed:
            
                if b > 0:
                    for c in storeName:
                        itemCheck = tempOrder.tempItemList1[0]
                        print(itemCheck)
                        tempList = store.searchNode(c)
                        tempList.sortStore()
                    
                        result = tempList.search(itemCheck)
                        if result == True:
                            
                            buyList.append(itemCheck)
                            if len(tempOrder.tempItemList1)>=1:
                                tempOrder.tempItemList1.pop(0)
                            break
                        
                elif len(tempOrder.tempItemList1)>=1 : 
                    tempOrder.tempItemList1.pop(0)
                    '''
    bought = []
    buyInDay = []
    tempBuyInDay = []
    needBuy = []
    quantityList = []
    daysCount = 0
    canDeli = []
       
    def delivery(self):
        for a in testName:
            tempOrder = order.searchNode(a) #search to house
            tempNeed = tempOrder.need       #take order list from house
            
            for i in storeName: 
                tempList1 = store.searchNode(i) #search store
                tempList1.sortStore()           #sort item list in store

                for b in tempNeed: #take quantity from order list
                    if b>0 :  #if quantity of item is 1 or 2 
                        itemCheck = tempOrder.tempItemList1[0] #take  item from list of item from house corresponding with quantity from order list at that position

                        check = tempList1.search(itemCheck) #search item in item list of store
                        if check == True: 
                            tempOrder.tempItemList.remove(check) #remove item from temp list in house
                            buyInDay.append(check) #put item into list of product to buy in store  
                            quantityList.append(b) #quantity of that item
                    if daysCount == 1:   # when shopping at 2 shop in 2 days 
                        if not tempOrder.tempItemList : # if items were removed in tempList => all item found and bought => done and delivery
                            bought = buyInDay  + bought
                            itemDeli = bought
                            bought = []
                            daysCount = 0
                            break
                        else:         
                            needBuy = needBuy + bought
                            bought = buyInDay
                            buyInDay = []  
                    if daysCount ==0:
                        bought = buyInDay  + bought  #add item buy each day into list of item bought 
                        buyInDay = []
                    
                    daysCount = daysCount + 1 
                    if not tempOrder.tempItemList : # if items were removed in tempList => all item found and bought => done and delivery
                        itemDeli = bought
                        
                        bought = []
                        daysCount = 0  
                    
                
                    
                   
                    
                        
                               
               

                    

       
                
    
    
               
                        
                         
                        
                        

        
    

      
toDO()

#tempFinal = tempBill.order
#print(tempFinal)



    
    



    




#ans = input("Enter Item  : ")



#print(result)
#if checkinStore(ans) == True:
#    print("yes")
#storeB.traverse()









    





