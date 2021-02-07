import csv
from Store  import Store
from Order  import Order
from LinkList import Node
from LinkList import  DoublyLinkedList

class Reader: #read file from csv
    
    def __init__(self, store, order): #insert data from shoplist into stores
        with open('shoplist.csv') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            row1 = next(reader)

            tempItemA = []
            tempItemB = []
            tempItemC = []
            for col in reader:
                tempItem = col[1]
                if col[3] == "Y": 
                    tempItemA.append(tempItem)
                if col[4] == "Y": 
                    tempItemB.append(tempItem)
                if col[5] == "Y":
                    tempItemC.append(tempItem)

           
            
            tempStoreA = Store(tempItemA, row1[3])
            tempStoreB = Store(tempItemB, row1[4])
            tempStoreC = Store(tempItemC, row1[5])
            store.insertToList(tempStoreA)
            store.insertToList(tempStoreB)
            store.insertToList(tempStoreC)

        with open('householdlist.csv') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            
            #deal with first and second lines of file
            tempName = next(reader) #take list of house numbers
            tempName.pop(0)
            row2 = next(reader)

            #add order from file to linklist    
            
            item = []
            orderlist = []
            tempOrder = []
            tempItem = []
            tempOrder1 = []
           
            count1 = 1  #count for variable in orderlist
            count2 = 0  #count for variable in tempName
            for col in reader:
                orderlist.append(col)
            
            
            while count1<8: #loop b<8 for first week
                for x in orderlist:
                    
                    tempItem.append(x[0])
                    if x[count1] == "":
                        tempOrder.append(0)
                    elif x[count1] == "1":
                        tempOrder.append(1)
                    elif x[count1] == "2":
                        tempOrder.append(2)

                   
                count1= count1+1
                
              
                
                tempHouse = Order(tempName[count2],tempItem, tempOrder)
                
                order.insertToList(tempHouse)
               
                count2= count2 + 1
                
                tempOrder = []
                tempItem  = []

    def readNameList(self):
         with open('householdlist.csv') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            
            #deal with first and second lines of file
            tempName = next(reader) #take list of house numbers
            tempName.pop(0)
            return tempName

    def readItemList(self):
        with open('shoplist.csv') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            row1 = next(reader)
            row1.pop(0)
            row1.pop(0)
            row1.pop(0)
            tempStoreName = []
            for i in row1:
                tempStoreName.append(i)
            
            tempItemList = []
            tempCostList = []
            tempProductList = []
            for col in reader:
                tempItemList.append(col[1])
                tempCostList.append(col[2])
                
                
            
            return tempItemList, tempCostList, tempStoreName
    
    

            
        