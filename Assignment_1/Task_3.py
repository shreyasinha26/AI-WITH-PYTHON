products = [10, 14, 22, 33, 44, 13, 22, 55, 66, 77]
total = 0
while True:
    ch = int(input("Please select product (1-10) 0 to Quit: "))
    if ch == 0:
        break
    if 1 <= ch <= 10:
        price = products[ch - 1]
        total += price
        print("Product:", ch, "Price:", price)

print("Total:", total)
payment = int(input("Payment: "))
print("Change:", payment - total)
