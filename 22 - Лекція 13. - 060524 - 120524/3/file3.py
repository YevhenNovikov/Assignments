class Car:

    def __init__(self, brand: str, model: str, year: int, speed: int):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed



    def accelerate(self):
        self.speed += 5
        

    def brake(self):

        if self.speed >= 5:
            self.speed -= 5
        else:
            self.speed = 0



    def display_speed(self):
        print(f"The speed of the {self.brand} {self.model} is {self.speed} km/h.")


my_car = Car('Aston Martin', 'DB 2/4 Mark III Drophead Coupé', 1959, 0)
my_car.accelerate()
my_car.display_speed()
my_car.accelerate()
my_car.display_speed()
my_car.accelerate()
my_car.display_speed()
my_car.accelerate()
my_car.display_speed()
my_car.accelerate()
my_car.display_speed()
my_car.accelerate()
my_car.display_speed()
my_car.brake()
my_car.display_speed()
my_car.brake()
my_car.display_speed()
my_car.brake()
my_car.display_speed()
my_car.brake()
my_car.display_speed()
my_car.brake()
my_car.display_speed()
my_car.brake()
my_car.display_speed()
my_car.brake()
my_car.display_speed()
