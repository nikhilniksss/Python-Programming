# classes and objects

class car:

    def start(self):
        print("Starting the engine")

car1 = car()
type(car1)

car1.start()

# init function

class Car:

    color = 'Red' # global variable

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def start(self):
        print("Starting the engine")


car1 = Car("Mahindra","XUV300",2020)
type(car1)

print(car1.make)
print(car1.model)
print(car1.speed)
print(car1.year)
print(car1.color)

