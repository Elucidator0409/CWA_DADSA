import csv

from Store  import Store
from Order  import Order
from Reader import Reader
from LinkList import Node
from LinkList import  DoublyLinkedList


    
    

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









    





