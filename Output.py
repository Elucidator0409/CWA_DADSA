
class Output:
    def __init__(self, item, order,houselist)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday"]
    print("Shopping Schedule")
    print("Week 1")
    for a in days:
        print(a)
        print (item + ", "+ order)
        input("Press Enter to continue...")

    print("Delivery Schedule")
    print("Week 1")
    for a in days:
        print(a)
        for x in houselist:
            print(x + ", ")
        input("Press Enter to continue...")

