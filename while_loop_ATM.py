#balance start at 1000
#user can deposit,withdraw or check balance,loop continues untill user enters exit

total = 1000

while True:
    value = input("Enter deposit, withdraw, or exit: ").lower()

    if value == "deposit":
        amount = float(input("Amount to deposit: "))
        if amount > 0:
            total += amount
            print("Balance:", total)
        else:
            print("Enter a positive amount!")

    elif value == "withdraw":
        amount = float(input("Amount to withdraw: "))
        if amount <= 0:
            print("Enter a positive amount!")
        elif amount > total:
            print("Insufficient balance! Your balance is:", total)
        else:
            total -= amount
            print("Balance:", total)

    elif value == "exit":
        print("Exiting...")
        break

    else:
        print("Invalid option!")