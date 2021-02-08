import csv
from Store  import Store
from House  import House
from LinkList import Node
from LinkList import  DoublyLinkedList

class Reader: #read file from csv
    
    def __init__(self, store, house): #insert data from shoplist into stores
        with open('shoplist.csv') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            header = next(reader) #take name for stores

            itemInA = []
            itemInB = []
            itemInC = []
            for col in reader:
                tempItem = col[1]
                if col[3] == "Y": 
                    itemInA.append(tempItem)
                if col[4] == "Y": 
                    itemInB.append(tempItem)
                if col[5] == "Y":
                    itemInC.append(tempItem)

           
            
            tempStoreA = Store(itemInA, header[3])
            tempStoreB = Store(itemInB, header[4])
            tempStoreC = Store(itemInC, header[5])
            store.insertToList(tempStoreA)
            store.insertToList(tempStoreB)
            store.insertToList(tempStoreC)

        with open('householdlist.csv') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            
            #deal with first and second lines of file
            tempName = next(reader) #take list of house numbers
            tempName.pop(0)
            
            next(reader) #skip lines 2 

            #add order from file to linklist    
            
            data = []
            tempOrder = []
            tempItem = []
           
            count1 = 1  #count for variable in data
            count2 = 0  #count for variable in tempName
            for col in reader:
                data.append(col)
            
            
            while count1<8: #loop b<8 for first week
                for x in data:
                    
                    tempItem.append(x[0])
                    if x[count1] == "":
                        tempOrder.append(0)
                    elif x[count1] == "1":
                        tempOrder.append(1)
                    elif x[count1] == "2":
                        tempOrder.append(2)
                count1= count1+1
                
              
                
                tempHouse = House(tempName[count2],tempItem, tempOrder)
                house.insertToList(tempHouse)
               
                count2= count2 + 1
                
                tempOrder = []
                tempItem  = []

    def readHouseNumList(self):
         with open('householdlist.csv') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            
            #deal with first and second lines of file
            houseNum = next(reader) #take list of house numbers
            houseNum.pop(0)

            for i in range(0, 7):
                houseNum.pop(0)
            return houseNum

    def readItemList(self):
        with open('shoplist.csv') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            header = next(reader)
            header.pop(0)
            header.pop(0)
            header.pop(0)
            
            storeName = []
            for i in header:
                storeName.append(i)
            
            listOfItemName = []
            listOfCosts = []
            for col in reader:
                listOfItemName.append(col[1])
                listOfCosts.append(col[2])
            
            return listOfItemName, listOfCosts, storeName
    
    

            
        