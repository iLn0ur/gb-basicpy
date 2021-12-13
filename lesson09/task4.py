class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self, speed=None):
        if speed is not None:
            self.speed = speed
            print(f'{self.name} go, speed: {self.speed}')
        else:
            print(f'{self.name} go, speed: {self.speed}')

    def turn(self, direction):
        print(f'{self.name} turn on {direction}')

    def stop(self):
        print(f'{self.name} stopped')
        self.speed = 0

    def show_speed(self):
        print(f'{self.name} speed is {self.speed}')


class TownCar(Car):

    def show_speed(self):
        if int(self.speed) > 60:
            print(f"{self.name} превышение скорости на {60 - int(self.speed)}")


class WorkCar(Car):

    def show_speed(self):
        if int(self.speed) > 40:
            print(f"превышение скорости на {40 - int(self.speed)}")


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police=True)


class SportCar(Car):
    pass


isuzu = WorkCar('isuzu', 'black', 35)
toyota = TownCar('toyota', 'red', 69)
bmw = SportCar('bmw', 'yellow', 99)
ford = PoliceCar('ford', 'blue', 101)

isuzu.turn('left')
toyota.show_speed()
bmw.stop()
ford.go(121)
bmw.show_speed()
toyota.go()

