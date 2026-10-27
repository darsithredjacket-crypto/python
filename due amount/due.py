due_amount=int(input("enter the due amount:"))
paid_amount=int(input("enter the paid amount:"))
if paid_amount==due_amount:
    print("you have paid the due amount")
elif paid_amount>due_amount:
    change=paid_amount-due_amount
    print(f"you have paid extra by:{change}")
elif paid_amount<due_amount:
    due=due_amount-paid_amount
    print(f"you are short by:{due}")
else:
    print("yo havent not paid any money")