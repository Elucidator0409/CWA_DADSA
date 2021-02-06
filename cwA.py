import csv

from Store  import Store
from Order  import Order
from Reader import Reader
from LinkList import Node
from LinkList import  DoublyLinkedList

def main():
    #method for usage
    def checkInStore(item):
        #check if item is in the store
        #use binary search, based on the fact that the items are sorted
        return binary_search(0, item.item.len(), item)

    def sortStore(item):
        #sort the items in the store for faster searching (binary search)
        
        # This value of i corresponds to how many values were sorted
        for i in range(len(item)):
        # We assume that the first item of the unsorted segment is the smallest
            lowest_value_index = i
        # This loop iterates over the unsorted items
        for j in range(i + 1, len(item)):
            if item[j] < item[lowest_value_index]:
                lowest_value_index = j
        # Swap values of the lowest unsorted element with the first unsorted
        # element
        item[i], item[lowest_value_index] = item[lowest_value_index], item[i]
        return

    
    ############################
    #algorithm methods

    def binary_search(self, low, high, x):
    #Recursive case
        if (high >= low):
            mid = (high + low) // 2
    
            #If element is at the middle -> found the value
            if self.item[mid] == x:
                return True
            #If element is smaller than the middle value -> search in the lower half
            elif self.item[mid] > x:
                return binary_search(arr, low, mid - 1, x)
            #If element is larger than the middle value -> search in the upper half
            else:
                return binary_search(arr, mid + 1, high, x)
            
        else:
            # Element is not present in the array
            return False


    def quick_sort():
        return;

    
    

'''
__MAIN__
'''
   
order = DoublyLinkedList()
store = DoublyLinkedList()

Reader(store, order)

ans = input("Enter Item  : ")
#b = result.name
#print(b)
main()
sortStore(ans)


#print(result)
if checkinStore(ans) == True:
    print("yes")
#storeB.traverse()









    





