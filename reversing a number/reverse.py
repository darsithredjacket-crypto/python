num=int(input("enter a number:"))
sum=0
rev=num
while rev>0:
    digit=rev%10
    sum=(sum*10)+digit
    rev//=10
print("\nreversed number=",sum)