#Task 1
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    def describe_car(self):
        print(f'{self.year}, {self.make}, {self.model}')


#Task 2
car = Car("Toyota", "Corolla", 2020)
car.describe_car()