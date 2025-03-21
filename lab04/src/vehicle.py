class vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self._speed = 0

    def drive(self, distance):
        self.mileage += distance
        print("Driving", distance, "km")

    def accelerate(self, increment):
        self._speed += increment
        print("Accelerating by", increment, "km/h")

    def decelerate(self, decrement):
        if self._speed - decrement >= 0:
            self._speed -= decrement
        else:
            self._speed = 0
        print("Decelerating by", decrement, "km/h")

    def display_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
        print("Mileage:", self.mileage)
        print("Current speed:", self._speed)


class Car(vehicle):
    def __init__(self, brand, model, year, fuel_type):
        super().__init__(brand, model, year)
        self.fuel_type = fuel_type
        self.is_engine_on = False

    def start_engine(self):
        self.is_engine_on = True
        print("Engine started")

    def stop_engine(self):
        self.is_engine_on = False
        print("Engine stopped")

    def display_info(self):
        super().display_info()
        print("Fuel type:", self.fuel_type)
        print("Engine status:", "On" if self.is_engine_on else "Off")

    @staticmethod
    def maintenance():
        print("Performing maintenance check")

    @classmethod
    def create_default(cls):
        return cls("DefaultBrand", "DefaultModel", 2000, "Unknown")


def main():
    car1 = Car("Toyota", "Corolla", 2010, "Petrol")
    car1.start_engine()
    car1.drive(150)
    car1.accelerate(20)
    car1.decelerate(5)
    car1.display_info()
    default_car = Car.create_default()
    default_car.display_info()
    unused_var = 123
    Car.maintenance()


if __name__ == "__main__":
    main()
