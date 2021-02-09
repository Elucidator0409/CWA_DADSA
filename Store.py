class Store:    
    #Constructors
    def __init__(self, item, name):
        #items will not be duplicated, this is enforced by the user
        self.item = item
        self.name = name
    
    #method for usage
   

    def sortStore(self):
        #sort the items in the store for faster searching (binary search)
       
        n = len(self.item)

        for i in range(n):
        # Create a flag that will allow the function to
        # terminate early if there's nothing left to sort
            already_sorted = True

        # Start looking at each item of the list one by one,
        # comparing it with its adjacent value. With each
        # iteration, the portion of the self.item that you look at
        # shrinks because the remaining items have already been
        # sorted.
            for j in range(n - i - 1):
                if self.item[j] > self.item[j + 1]:
                # If the item you're looking at is greater than its
                # adjacent value, then swap them
                    self.item[j], self.item[j + 1] = self.item[j + 1], self.item[j]

                # Since you had to swap two elements,
                # set the `already_sorted` flag to `False` so the
                # algorithm doesn't finish prematurely
                    already_sorted = False

        # If there were no swaps during the last iteration,
        # the self.item is already sorted, and you can terminate
            if already_sorted:
                break

        return self.item
            

    
    ############################
    #algorithm methods

    def search(self,item):
	    first = 0
	    last = len(self.item)-1
	    found = False
	    while( first<=last and not found):
		    mid = (first + last)//2
		    if self.item[mid] == item :
			    found = True
		    else:
			    if item < self.item[mid]:
				    last = mid - 1
			    else:
				    first = mid + 1	
	    return found

    def quick_sort(self):
        return