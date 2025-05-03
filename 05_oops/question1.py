class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand


    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    @staticmethod
    def general_description():
        return "Cars are Cool 😼"

    

    def __str__(self):
        return f"{self.__brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def full_name(self):  # override the method
        parent_name = super().full_name()
        return f"{parent_name} | Battery: {self.battery_size}"

    def __str__(self):  # ✅ Properly indented now
        parent_str = super().__str__()
        return f"{parent_str} | Battery: {self.battery_size}"


class Battery:
    def batter_info(self):
        return " Battery 🙂"

class Engine:
    def engine_info(self):
        return " Engine 😆"


class ElectricCarTwo(Battery , Engine , Car):
    pass




my_tesla = ElectricCarTwo("tesla" , "Y")

print(my_tesla.engine_info())

# my_car = Car("Mahindra", "BE 09")

# print(my_car.general_description())



# my_ev_car = ElectricCar("BMW", " i7", "101.7 kWh")

# print(my_ev_car.get_brand())

# print(Car.total_car)
