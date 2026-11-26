class lamborghini:
    def __init__(self):
        self.name="lamboghini"
        self.speed=250
        self.mileage=25
class Audi:
    def __init__(self):
        self.name="audi"
        self.speed=340
        self.mileage=20
def compare_cars(car1,car2):
    if car1.speed>car2.speed:
        print(car1.name,"is faster")
    else:
        print(car2.name,"is faster")
    if car1.mileage>car2.mileage:
         print(car1.name,"has a better mileage")
    else:
        print(car2.name,"has a better mileage")
b=lamborghini()
f=Audi()
compare_cars(b,f)