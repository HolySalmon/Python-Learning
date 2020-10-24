# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:
    # atributes
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        return f'{self.name} поехал'

    def stop(self):
        return f'{self.name} остановился'

    def turn_right(self):
        return f'{self.name} повернул направо'

    def turn_left(self):
        return f'{self.name} повернул налево'

    def show_speed(self):
        return f'Текущая скорость автомобиля {self.name} равна = {self.speed}км/ч'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость городского автомобиля {self.name} равна = {self.speed}км/ч')

        if self.speed > 60:
            return f'Скорость автомобиля {self.name} больше разрешенной'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость рабочего автомобиля {self.name} равна = {self.speed}км/ч')

        if self.speed > 40:
            return f'Скорость автомобиля {self.name} больше разрешенной'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} - полицейский автомобиль'
        else:
            return f'{self.name} - гражданский автомобиль'


porshe = SportCar(120, 'Black', 'Porshe', False)
hyundai = TownCar(70, 'White', 'Hyundai', False)
kamaz = WorkCar(50, 'Orange', 'Kamaz', False)
ford = PoliceCar(100, 'Blue', 'Ford', True)

print(kamaz.turn_left())
print(f'Когда {hyundai.turn_right()}, {porshe.go()}')
print(f'{kamaz.go()}, двигается со скоростью {kamaz.show_speed()}')
print(f'{kamaz.name} is {kamaz.color}')
print(f'{hyundai.name} полицейский автомобиль? {hyundai.is_police}')
print(f'{ford.name} полицейский автомобиль? {ford.is_police}')
print(porshe.show_speed())
print(hyundai.show_speed())
print(ford.show_speed())