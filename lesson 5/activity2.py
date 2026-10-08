actual_cost=float(input("please enter the products actual price:"))
sales_amount=float(input("please enter the slaes amount:" ))
if(sales_amount>actual_cost):
    amount=sales_amount-actual_cost
    print("total profit={0}".format(amount))
else:
    print("no profit!!")
