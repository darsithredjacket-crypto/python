lower=int(input("enter a lower range:"))
upper=int(input("enter an upper range:"))
count=0
print("prime numbers between",lower,"and",upper,"are:")
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if(num % i) == 0:
                break
        else:
            count=count+1
print("\nthe number of prime numbers are:",count)
