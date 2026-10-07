amt=int(input("please enter the required amount for withdrawel:"))
note_1=amt//100
note_2=(amt%100)//50
note_3=((amt%100)%50)//10
print("notes of 100 rupee", note_1)
print("notes of 50 rupee", note_2)
print("notes of 10 rupee", note_3)
