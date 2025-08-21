def tester(givenstring="Too short"):
    print(givenstring)

while True:
    enter=input("Write something (quit ends): ")
    if enter=="quit":
        break
    if len(enter)<10:
        tester()
    else:
        tester(enter)