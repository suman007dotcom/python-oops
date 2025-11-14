class car():
    def __init__(self,brand,mileage,fuel_type):
        self.brand = brand
        self.mileage = mileage
        self.fuel_type = fuel_type
    def start_engine(self):
        print(f"engine started for {self.brand}")
car1 = car("volkswagen virtus", 18.45, "diesel")
car1.start_engine()