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
    
    buyList = []
    
    
    
    for i in range(0, 27):
        tempProduct = Product(itemList[i], costList[i])
        productList.append(tempProduct)
    tempProductList = productList
    
   
    #for y in tempProductList:
        #print(y.name+"    "+ y.cost)
    count = 0

    
    testName=["1A"]   
    
    for a in testName:
        tempOrder = order.searchNode(a)
        tempNeed = tempOrder.need
        tempItem = tempOrder.itemlist
        
        for b in tempNeed:
            
                if b > 0:
                    for c in storeName:
                        itemCheck = tempItem[0]
                        
                        tempList = store.searchNode(c)
                        tempList.sortStore()
                    
                        result = tempList.search(itemCheck)
                        if result == True:
                            
                            buyList.append(itemCheck)
                            if len(tempItem)>=1:
                                tempItem.pop(0)
                            break
                        
                elif len(tempItem)>=1 : 
                    tempItem.pop(0)
        
    for z in buyList:
        print(z)
    
               
                        
                         
                        
                        

        
    

      
toDO()

#tempFinal = tempBill.order
#print(tempFinal)



    
    



    




#ans = input("Enter Item  : ")



#print(result)
#if checkinStore(ans) == True:
#    print("yes")
#storeB.traverse()









    





