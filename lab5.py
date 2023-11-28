class Engine:

    def __init__(self, power: int, company: str):
        self.power = power
        self.company = company

    def __str__(self):
        return f'Мотор: {self.power} л.с., {self.company}'

class Driver:

    def __init__(self, name: str, surname: str, experience: int):
        self.name = name
        self.surname = surname
        self.experience = experience

    def __str__(self):
        return f'Водитель: {self.name, self.surname}, Стаж вождения: {self.experience}'

class Person:

    def __init__(self, name: Driver, surname: Driver, age: int):
        self.name = name
        self.surname = surname
        self.age = age


class Car:

    def __init__(self, car_brand: str, car_class: str, car_weight: int, name: Driver, surname: Driver, experience: Driver, power: Engine, company: Engine):
        self.car_brand = car_brand
        self.car_class = car_class
        self.car_weight = car_weight
        self.name = name
        self.surname = surname
        self.experience = experience
        self.power = power
        self.company = company

    def __str__(self):
        return f"""
Марка: {self.car_brand}
Класс: {self.car_class}
Вес: {self.car_weight}
Водитель: {self.name} {self.surname}
Стаж вождения: {self.experience}
Мотор: {self.power} л.с., {self.company}"""

    def start(self) -> None:
        print('Поехали')

    def stop(self) -> None:
        print('Останавливаемся')

    def turn_right(self) -> None:
        print('Поворот направо')

    def turn_left(self) -> None:
        print('Поворот налево')

class Lorry:

    def __init__(self, car_brand: Car, car_class: Car, car_weight: Car, name: Driver, surname: Driver, experience: Driver, power: Engine, company: Engine, truck_weight: int) -> None:
        self.car_brand = car_brand
        self.car_class = car_class
        self.car_weight = car_weight
        self.name = name
        self.surname = surname
        self.experience = experience
        self.power = power
        self.company = company
        self.truck_weight = truck_weight

    def __str__(self):
        return f"""
Марка: {self.car_brand}
Класс: {self.car_class}
Вес: {self.car_weight}
Водитель: {self.name} {self.surname}
Стаж вождения: {self.experience}
Мотор: {self.power} л.с., {self.company}
Грузоподъемность: {self.truck_weight} кг"""

class SportCar:

    def __init__(self, car_brand: Car, car_class: Car, car_weight: Car, name: Driver, surname: Driver, experience: Driver, power: Engine, company: Engine, sport_car_speed: int) -> None:
        self.car_brand = car_brand
        self.car_class = car_class
        self.car_weight = car_weight
        self.name = name
        self.surname = surname
        self.experience = experience
        self.power = power
        self.company = company
        self.sport_car_speed = sport_car_speed

    def __str__(self):
            return f"""
Марка: {self.car_brand}
Класс: {self.car_class}
Вес: {self.car_weight}
Водитель: {self.name} {self.surname}
Стаж вождения: {self.experience}
Мотор: {self.power} л.с., {self.company}
Предельная скорость: {self.sport_car_speed} км/ч"""

    def nonen(self):
        pass

engine = Engine(1000,'Toyota')
driver = Driver('Иван', 'Ivanov', 15)
car = Car(car_brand='Toyota Camry', car_class='Sedan', car_weight=2000, name=driver.name, surname=driver.surname, experience=driver.experience, power=engine.power, company=engine.company)
truck = Lorry(car_brand='Kenworth', car_class='Truck', car_weight=10000, name=driver.name, surname=driver.surname, experience=driver.experience, power=engine.power, company=engine.company,truck_weight=50000)
sport = SportCar(car_brand='SSC Tuatara', car_class='Sport car', car_weight=3000, name=driver.name, surname=driver.surname, experience=driver.experience, power=engine.power, company=engine.company,sport_car_speed=480)

print(car)
print(truck)
print(sport)