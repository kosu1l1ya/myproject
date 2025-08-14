class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def display_info(self):
        print(
            f'Название автомобиля: {self.name} Скорость: {self.max_speed} Пробег: {self.mileage}')

    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name} {capacity} пассажиров"


class Autobus(Transport):
    def seating_capacity(self, capacity=50):
        return f"Вместимость одного автобуса {self.name} {capacity} пассажиров"


a = Autobus('e', 4, 60)
print(a.seating_capacity())
