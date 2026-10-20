n=int(input("enter a number:"))
binary=0
i=1
while n>0:
    r=n%2
    binary=(r*i)+binary
    n=n//2
    i=i*10
print("binary number",binary)