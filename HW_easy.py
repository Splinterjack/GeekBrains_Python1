# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

class TownCar:
    def __init__(self, color, name, is_police=0):
        self.color = color
        self.name = name
        self.is_police = int(is_police)

    def go(self):
        print(f"Машина {self.name} едет!")

    def stop(self):
        print(f"Машина {self.name} остановилась!")

    def turn(self, side):
        if side == "left":
            side = "налево"
            print(f"Машина {self.name} повернула {side}!")
        elif side == "right":
            side = "направо"
            print(f"Машина {self.name} повернула {side}!")
        else:
            print("Указано неверное направление!")
            pass


class SportCar:
    def __init__(self, color, name, is_police=0):
        self.color = color
        self.name = name
        self.is_police = int(is_police)

    def go(self, name):
        print(f"Машина {self.name} едет!")

    def stop(self, name):
        print(f"Машина {self.name} остановилась!")

    def turn(self, side):
        if side == "left":
            side = "налево"
            print(f"Машина {self.name} повернула {side}!")
        elif side == "right":
            side = "направо"
            print(f"Машина {self.name} повернула {side}!")
        else:
            print("Указано неверное направление!")
            pass


class WorkCar:
    def __init__(self, color, name, is_police=0):
        self.color = color
        self.name = name
        self.is_police = int(is_police)

    def go(self, name):
        print(f"Машина {self.name} едет!")

    def stop(self, name):
        print(f"Машина {self.name} остановилась!")

    def turn(self, side):
        if side == "left":
            side = "налево"
            print(f"Машина {self.name} повернула {side}!")
        elif side == "right":
            side = "направо"
            print(f"Машина {self.name} повернула {side}!")
        else:
            print("Указано неверное направление!")
            pass


class PoliceCar:
    def __init__(self, color, name, is_police=1):
        self.color = color
        self.name = name
        self.is_police = int(is_police)

    def go(self):
        print(f"Машина {self.name} едет!")

    def stop(self):
        print(f"Машина {self.name} остановилась!")

    def turn(self, side):
        if side == "left":
            side = "налево"
            print(f"Машина {self.name} повернула {side}!")
        elif side == "right":
            side = "направо"
            print(f"Машина {self.name} повернула {side}!")
        else:
            print("Указано неверное направление!")
            pass

        print(f"Машина {self.name} повернула {side}!")


car2 = TownCar("red", "Mazda", 0)
car2.turn("ппро")
print(car2.name)
# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car:
    def __init__(self, color, name, is_police):
        self.color = color
        self.name = name
        self.is_police = int(is_police)

    def go(self):
        print(f"Машина {self.name} едет!")

    def stop(self):
        print(f"Машина {self.name} остановилась!")

    def turn(self, side):
        if side == "left":
            side = "налево"
            print(f"Машина {self.name} повернула {side}!")
        elif side == "right":
            side = "направо"
            print(f"Машина {self.name} повернула {side}!")
        else:
            print("Указано неверное направление!")
            pass


class TownCar(Car):
    def __init__(self, color, name, is_police, body_type, engine_type):
        super().__init__(color, name, is_police)
        self.is_police = "0"
        self.body_type = body_type
        self.engine_type = engine_type

    def body_type(self):
        return self.body_type

    def engine(self):
        return self.engine


class SportCar(Car):
    def __init__(self, color, name, is_police, race_type, power):
        super().__init__(color, name, is_police)
        self.is_police = "0"
        self.race_type = race_type
        self.power = int(power)

    def race_type(self):
        print(self.race_type)

    def my_power(self):
        print(self.power, "hp")


car1 = TownCar("green", "Volvo", "0", "sedan", "gas")
car3 = SportCar("silver", "Nissan", "0", "GT", "324")
car3.my_power()