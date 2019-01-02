items =["T-shirt", "Sweater"]

loop = True

while loop:
    order = input("Welcome to our shop, what do you want (C, R, U, D)? ")
    

    if order == "R" or order == "r":
        print(items)
        
    elif order == "C" or order == "c":
        
        new_item = input("Enter new item")
            
        items.append(new_item)
        print(items)
        for i in items:
            print("Our items:", items)
            print(i)

    elif order == "U" or order == "u":
        
        position_update = input("Update position?")
        update_item = input("New item?")
            
        items[int(position_update)] = update_item
        print(items[int(position_update)])
        for i in items:
            print("Our items:", items)
            print(i)

    elif order == "D" or order == "d":
        
        position_delete = input("Delete position?")
            

        items.pop(int(position_delete))
        for i in items:
            print("Our items:", items)
            print(i)
        loop = False

