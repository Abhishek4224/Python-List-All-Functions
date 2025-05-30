num = []
while True:
    print("################  MAIN MENU  ################")
    print("Press 1 for Adding of element")
    print("Press 2 for Printing of element")
    print("Press 3 for Deletion of element")
    print("Press 4 for Modifying of an element")
    print("Press 5 for Inserting of an element")
    print("Press 6 for Exit")
    
    ch = int(input("Enter your choice = "))
    if ch == 1:
        print("################## Adding Element in the list  ################")
        ch1 = "y"
        while ch1 == "y":
            n=input("Enter element to append = ")
            num.append(n)
            ch1 = input("Any more data (y/n) = ")
    elif ch == 2:
        print("################## Reading Element from the list  ################")
        print("Press 1 for Existing order ")
        print("Press 2 for Reverse order")
        print("Press 3 for Ascending order")
        print("Press 4 for descending order")
        k = int(input("Enter your Choice = "))
        if k == 1:
            print(num)
        if k == 2:
            num.reverse()
            print(num)
        if k == 3:
            num.sort()
            print(num)
        if k == 4:
            num.sort(reverse=True)
            print(num)
            
    elif ch == 3:
        print("################## Deleting Element from the list  ################")
        print("Press 1 for deletion by element ")
        print("Press 2 for deletion by Position ")
        k = int(input("Enter your choice = "))
        if k == 1:
            print("Current list : ",num)
            el = input("Enter element to delete = ")
            num.remove(el)
            print(num)
        else:
            print("Current list : ",num)
            pos = int(input("Enter Position of Element to delete = "))
            num.pop(pos)
            print(num)
    elif ch == 4:
        print("################## Modifying Element from the list  ################")
        print("Current List :", num)
        pos = int(input("Enter Position = "))
        element = input("Enter Element = ")
        num[pos] = element
        print("List after Modification : ", num)
        
    elif ch == 5:
        print("################## Modifying Element from the list  ################")
        print("Current List :", num)
        pos = int(input("Enter the position of element to insert : "))
        element =  input("Enter Element to insert : ")
        num.insert(pos,element)
        print("List after Insertion of element : ", num)
        
    elif ch == 6:
        print("Bye Bye..")
        break
        
        
        
            
        
        
            
            
        
    
    