class dog:
    animal="dog"
    def __init__(self, breed, age):
        self.breed=breed
        self.age=age
    def display(self):
        print("animal:", dog.animal)
        print("breed:", self.breed)
        print("age:", self.age)
        print()
dog1=dog("labrador", 3)
dog2=dog("german shepherd", 5)
dog1.display()
dog2.display()