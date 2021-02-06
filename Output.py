
class Output:
    def __init__(self, itemList, quantityList,houselist)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday"]
    print("Shopping Schedule")
    print("Week 1")
    for a in days:
        print(a)
        for item, quantity in zip(itemList, quantityList):
            print (item) ,"", (quantity)
        input("Press Enter to continue...")

    print("Delivery Schedule")
    print("Week 1")
    for a in days:
        print(a)
        for x in houselist:
            print(x + ", ")
        input("Press Enter to continue...")

