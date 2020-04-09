class Check_methods:
    wheels = 4
    def __init__(self,price,brand):
        self.price = price
        self.brand = brand
    
    @classmethod
    def honk(cls):
        return ("The car honks")
    
    @staticmethod
    def moves():
        print("The car is moving")
    
    def show(self):
        print(self.price,self.brand)

if __name__ == "__main__":
    car1 = Check_methods(20000,"BMW")
    car2 = Check_methods(50000,"Benz")
    print(car1.price,car1.brand,car1.wheels)
    print(car2.price,car2.brand)
    print(Check_methods.honk())
    car1.show()
    Check_methods.moves()
