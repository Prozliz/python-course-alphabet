"""
Вам небхідно написати 3 класи. Колекціонери Гаражі та Автомобілі.
Звязкок наступний один колекціонер може мати багато гаражів.
В одному гаражі може знаходитися багато автомобілів.

Автомобіль має наступні характеристики:
    price - значення типу float. Всі ціни за дефолтом в одній валюті.
    type - одне з перечисленних значеннь з CARS_TYPES в docs.
    producer - одне з перечисленних значеннь в CARS_PRODUCER.
    number - значення типу UUID. Присвоюється автоматично при створенні автомобілю.
    mileage - значення типу float. Пробіг автомобіля в кілометрах.


    Автомобілі можна перівнювати між собою за ціною.
    При виводі(logs, print) автомобілю повинні зазначатися всі його атрибути.

    Автомобіль має метод заміни номеру.
    номер повинен відповідати UUID

Гараж має наступні характеристики:

    town - одне з перечислениз значеннь в TOWNS
    cars - список з усіх автомобілів які знаходяться в гаражі
    places - значення типу int. Максимально допустима кількість автомобілів в гаражі
    owner - значення типу UUID. За дефолтом None.


    Повинен мати реалізованими наступні методи

    add(car) -> Добавляє машину в гараж, якщо є вільні місця
    remove(cat) -> Забирає машину з гаражу.
    hit_hat() -> Вертає сумарну вартість всіх машин в гаражі


Колекціонер має наступні характеристики
    name - значення типу str. Його ім'я
    garages - список з усіх гаражів які належать цьому Колекціонеру. Кількість гаражів за замовчуванням - 0
    register_id - UUID; Унікальна айдішка Колекціонера.

    Повинні бути реалізовані наступні методи:
    hit_hat() - повертає ціну всіх його автомобілів.
    garages_count() - вертає кількість гаріжів.
    сars_count() - вертає кількість машиню
    add_car() - додає машину у вибраний гараж. Якщо гараж не вказаний, то додає в гараж, де найбільше вільних місць.
    Якщо вільних місць немає повинне вивести повідомлення про це.

    Колекціонерів можна порівнювати за ціною всіх їх автомобілів.
"""

import uuid
import random
from constants import *
class Car():

    def __init__(self, price: float,type,producer, milege:float,):
        self.price = price
        if type in CARS_TYPES:
            self.type = type
        if producer in CARS_PRODUCER:
            self.producer= producer
        self.number = uuid.uuid4()
        self.milege = milege



    def __eq__(self, other):
        return other.price == self.price

    def __lt__(self, other):
        return other.price < self.price

    def __gt__(self, other):
        return other.price < self.price
    def __str__(self):
        return "Car(%r, %r, %r, %r, %r)" % (self.price, self.type, self.producer, self.number, self.milege)

    def __repr__(self):
        return "Car(%r, %r, %r, %r, %r)" % (self.price, self.type, self.producer,self.number,self.milege)

    def change_number(self):
        self.number = str(uuid.uuid4())
        return "You new number", self.number

class Garage():
     def __init__(self,cars: list,town,places:int):
        if town in TOWNS:
            self.town = town
        self.cars = cars
        self.places = places - len(cars)
        self.owner = None
        self.counter = 0
     def add (self,new_car):
        if self.places != 0:
            self.cars += [new_car]
            self.places -= 1
            return 'Your car was add'
        else:
            return 'No more place'

     def remove(self,remove_car):
         self.cars.remove(remove_car)
         self.places += 1
         return 'Your car was removed'

     def hit_hap(self):
        all_price = 0
        for this_car in self.cars:
            for my_car in this_car:
             all_price += my_car.__dict__['price']
        return all_price


     def __iter__(self):
         return self

     def __next__(self):
         if self.counter< len(self.cars):
             my_car = self.cars[self.counter]
             self.counter+=1
             return my_car
         else:
             raise StopIteration


     def __str__(self):
        return "Garage(%r, %r, %r)" % (self.town, self.cars, self.places)


     def __repr__(self):
        return "Garage(%r, %r, %r)" % (self.town, self.cars, self.places)
class Collectioner():

    def __init__(self,name:str,garages=0):
        self.name = name
        self.garages = [garages]
        self.register_id = uuid.uuid4()
        self.counter =0
    def hit_hat(self):
        price_collectioner=0
        for a_car in self.garages:
            for only_car in a_car:
                price_collectioner+= only_car.__dict__['price']
        return price_collectioner


    def garages_count(self):
        return len(self.garages)

    def cars_count(self):
        count= 0
        for members in self.garages:
            for some in members:
                count+=1
        return count

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < len(self.garages):
            my_garages = self.garages[self.counter]
            self.counter += 1
            return my_garages
        else:
            raise StopIteration

    def add_car(self,new_car,garage=None):
        for garage_class in self.garages:
            if garage in self.garages:
                if garage.__dict__['places'] != 0:
                    garage.__dict__['cars'] += [new_car]
                    return 'Car was added'''
                else:
                    return 'No more place in garage.Choose next one'''

            else:
                a = 0
                if a<int(garage_class.__dict__['places']):
                    a = int(garage_class.__dict__['places'])
                if a == int(garage_class.__dict__['places']) and a!=0:
                    garage_class.__dict__['cars'] += [new_car]
                    return 'Car was added'
                else:
                    return 'No more place'




    def __str__(self):
        return "Collectioner(%r, %r, %r)" % (self.name, self.garages, self.register_id)

    def __repr__(self):
        return "Collectioner(%r, %r, %r)" % (self.name, self.garages, self.register_id)


