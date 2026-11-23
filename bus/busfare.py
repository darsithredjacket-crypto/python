class vehicle:
    def __init__(self,name,max_speed,capacity):
        self.name=name
        self.max_speed=max_speed
        self.capacity=capacity
    def busfare(self):
        return self.capacity*100
class bus(vehicle):
    def busfare(self):
        amount= super().busfare()
        amount+=amount*10/100
        return amount
obj= bus("school bus", 180, 50)
print("total busfare is:", obj.busfare())
