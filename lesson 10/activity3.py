n=int(input("enter a number:"))
s=str(n)
mid=len(s)//2
if len(s)%2==0:
    product= int(s[mid-1])*int(s[mid])
else:
    product=int(s[mid])
print("product=",product)