print("choose your ride")
choice1=int(input("choose 1 for car and 2 for bike:"))

if (choice1==1):
    choice2=input("choose 1 for sedan or 2 for suv:")
    if choice2==1:
        print("you've chosen a sedan")
    else:
        print("you've choesn a suv")
elif (choice1==2):
    choice2=input("choose 1 for scooter or 2 for scooty:")
    if choice2==1:
        print("you've choosen a scooter")
    else:
        print("you've choosen a scooty")
else:
    print("you've choosen an incorrect option")
