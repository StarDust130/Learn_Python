class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

    def __str__(self):  # magic method to print nicely
        return f"{self.brand} {self.model}"

my_car = Car("Mahindra", "BE 09")
print(my_car.full_name())  # Now prints: Mahindra BE 09


