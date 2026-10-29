try:
    age=int(input("enter an age:"))
    if type(age)==int:
        if age%2==0:
            print("this is an even number")
        else:
            print("this is an odd number")
except ValueError as ex:
    print("exception", ex)
