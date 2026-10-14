medical_cause=input("do u have a mediacl cause? (Y/N):").strip().upper()
if medical_cause=="Y":
    print("you are allowed")
else:
    atten=int(input("enter the attendence of the student:"))
    if atten>=75:
        print("allowed")
    else:
        print("not allowed")