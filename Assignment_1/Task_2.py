cart=[]
while True:
    ch=input("Would you like to \n(1)Add or \n(2)Remove items or  \n(3)Quit?")
    if ch=="1":
        item=input("What will be added?: ")
        cart.append(item)

    elif ch=="2":
        print(f"There are {len(cart)} items in the list.")
        index=int(input("Which item is deleted?: "))
        if 0 <= index < len(cart):
            cart.pop(index)
        else:
            print("Incorrect selection.")

    elif ch =="3":
        print("The following items remain in the list:")
        for item in cart:
            print(item)
        break
    else:
        print("Incorrect selection.")
