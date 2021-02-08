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
        tempOrder = order.searchNode(a) #search to house
        tempNeed = tempOrder.createCopy()  
         #take order list from house
        #print("do1")    
        for i in storeName: 
            tempList1 = store.searchNode(i) #search store
            tempList1.sortStore()           #sort item list in store
            tempList2 = tempOrder.itemlist 
            tempList3 = tempOrder.tempItemList
            
            #print("do2")
            for b in tempNeed: #take quantity from order list
                if b>0 :  #if quantity of item is 1 or 2 
                    print("START")
                    itemCheck = tempList2[0] #take  item from list of item from house corresponding with quantity from order list at that position
                    print("Item to search :"+itemCheck)
                    
                    check = tempList1.search(itemCheck) #search item in item list of store
                    
                   
                    if check == True: 
                        tempOrder.tempItemList.remove(itemCheck) #remove item from temp list in house
                        print("do")
                        for i in tempOrder.tempItemList: 
                            print(i)
                        buyInDay.append(itemCheck) #put item into list of product to buy in store 
                         
                elif len(tempList2)>=1:
                    tempList2.pop(0)
           
                    
                
                '''
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
                 
                   '''      
               
                

                if daysCount ==0 and check == True:
                    bought = buyInDay  + bought  #add item buy each day into list of item bought 
                   
                    buyInDay = []
                print("END ")
                
                
                     
                        
                    
                daysCount = daysCount + 1 
                if not tempOrder.tempItemList : # if items were removed in tempList => all item found and bought => done and delivery
                    itemDeli = bought
                    print("do4")
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









    





