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
    while is_done:  #MAIN ALGO
       

        for a in testName:
            tempOrder = order.searchNode(a)
            tempNeed = tempOrder.need
            
            for i in storeName: 
                tempList1 = store.searchNode(i)
                tempList1.sortStore()
      
                for b in tempNeed:
                    if b>0 :
                        
                        
                    
                        itemCheck = tempOrder.tempItemList1[0]
                        check = tempList1.search(itemCheck)
                        if check == True:
                            tempOrder.tempItemList.remove(check)
                            buyInDay.append(check) #c
                            quantityList.append(b)
                    if daysCount == 2:    
                        if not tempOrder.tempItemList :
                    
                            itemDeli = bought
                            bought = []
                            daysCount = 0
                        else:         
                            needBuy = needBuy + bought
                            bought = buyInDay
                            buyInDay = []  
                    bought = buyInDay  + bought  #a b c 
                    tempBuyInDay = buyInDay# C
                    
                    daysCount = daysCount + 1   
                    
                
                    
                   
                    
                        
                               
               

                    

       
                
    
    
               
                        
                         
                        
                        

        
    

      
toDO()

#tempFinal = tempBill.order
#print(tempFinal)



    
    



    




#ans = input("Enter Item  : ")



#print(result)
#if checkinStore(ans) == True:
#    print("yes")
#storeB.traverse()









    





