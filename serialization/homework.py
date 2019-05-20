"""
Для попереднього домашнього завдання.
Для класу Колекціонер Машина і Гараж написати методи, які створюють інстанс обєкту
    з (yaml, json, pickle) файлу відповідно  (десерылызацыя з файлу)

Для класів Колекціонер Машина і Гараж написати методи, які зберігають стан обєкту в файли формату
yaml, json, pickle відповідно.(серелызацыя в файл, дамп)

Для класів Колекціонер Машина і Гараж написати методи, які конвертують обєкт в строку формату
yaml, json, pickle відповідно.(сереизация дампс)

Для класу Колекціонер Машина і Гараж написати методи, які створюють інстанс обєкту
з (yaml, json, pickle) строки відповідно(десереалызация строки)


Advanced
Добавити опрацьовку формату ini

"""

import uuid
import json
import pickle
from ruamel.yaml import YAML
from constants import *


class Car():

    def __init__(self, price: float, type, producer, milege: float, number=uuid.uuid4()):
        self.price = price
        if type in CARS_TYPES:
            self.type = type
        if producer in CARS_PRODUCER:
            self.producer = producer
        self.number = number
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
        return "Car(%r, %r, %r, %r, %r)" % (self.price, self.type, self.producer, self.number, self.milege)

    def change_number(self):
        self.number = str(uuid.uuid4())
        return "You new number", self.number

    def convert_to_dict(self):
        obj_dict = {"__class__": self.__class__.__name__, "__module__": self.__module__}
        obj_dict.update(self.__dict__)
        return obj_dict


class Garage():
    def __init__(self, town, places: int, cars: list, owner=None, counter=0):
        if town in TOWNS:
            self.town = town
        self.cars = cars
        self.places = places - len(cars)
        self.owner = owner
        self.counter = 0

    def add(self, new_car):
        if self.places != 0:
            self.cars += [new_car]
            self.places -= 1
            return 'Your car was add'
        else:
            return 'No more place'

    def remove(self, remove_car):
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
        if self.counter < len(self.cars):
            my_car = self.cars[self.counter]
            self.counter += 1
            return my_car
        else:
            raise StopIteration

    def __str__(self):
        return "Garage(%r, %r, %r)" % (self.town, self.cars, self.places)

    def __repr__(self):
        return "Garage(%r, %r, %r)" % (self.town, self.cars, self.places)


class Collectioner():

    def __init__(self, name: str, garages=0, register_id=uuid.uuid4(), counter=0):
        self.name = name
        self.garages = [garages]
        self.register_id = register_id
        self.counter = counter

    def hit_hat(self):
        price_collectioner = 0
        for a_car in self.garages:
            for only_car in a_car:
                price_collectioner += only_car.__dict__['price']
        return price_collectioner

    def garages_count(self):
        return len(self.garages)

    def cars_count(self):
        count = 0
        for members in self.garages:
            for some in members:
                count += 1
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

    def add_car(self, new_car, garage=None):
        for garage_class in self.garages:
            if garage in self.garages:
                if garage.__dict__['places'] != 0:
                    garage.__dict__['cars'] += [new_car]
                    return 'Car was added'''
                else:
                    return 'No more place in garage.Choose next one'''

            else:
                a = 0
                if a < int(garage_class.__dict__['places']):
                    a = int(garage_class.__dict__['places'])
                if a == int(garage_class.__dict__['places']) and a != 0:
                    garage_class.__dict__['cars'] += [new_car]
                    return 'Car was added'
                else:
                    return 'No more place'

    def __str__(self):
        return "Collectioner(%r, %r, %r)" % (self.name, self.garages, self.register_id)

    def __repr__(self):
        return "Collectioner(%r, %r, %r)" % (self.name, self.garages, self.register_id)

    def convert_to_dict(self):
        obj_dict = {"__class__": self.__class__.__name__, "__module__": self.__module__}
        obj_dict.update(self.__dict__)
        return obj_dict



# ___________________JSON__________________

def convert_to_dict_car(obj):
    obj_dict = {"__class__": obj.__class__.__name__, "__module__": obj.__module__}
    obj_dict.update(obj.__dict__)
    obj_dict['number'] = str(obj_dict['number'])
    return obj_dict


def convert_to_dict_garage(obj):
    ser_car = []
    obj_dict = {"__class__": obj.__class__.__name__, "__module__": obj.__module__}
    obj_dict.update(obj.__dict__)
    for car in obj.cars:
        car = convert_to_dict_car(car)
        ser_car.append(car)
    obj_dict.update({'cars': ser_car})
    return obj_dict


def convert_to_dict_collectioner(obj):
    obj_dict = {"__class__": obj.__class__.__name__, "__module__": obj.__module__}
    obj_dict.update(obj.__dict__)
    obj_dict['register_id'] = str(obj_dict['register_id'])

    for garage in obj_dict['garages']:
        garage = convert_to_dict_garage(garage)
        obj_dict.update(({'garages': garage}))
    return obj_dict


def dict_to_object_car(our_dict):
    if "__class__" in our_dict:
        class_name = our_dict.pop("__class__")
        module_name = our_dict.pop("__module__")
        module = __import__(module_name)
        class_ = getattr(module, class_name)
        obj = class_(**our_dict)
    else:
        obj = our_dict
    return obj


# DUMPS
car1 = Car(12, "SUV", "BMW", 128)
car3 = Car(12, "SUV", "BMW", 123)
car2 = convert_to_dict_car(car1)
my_json_car1 = json.dumps(car2, indent=4)

garage1 = Garage('Kiev', 4, [car1, car3])

garage2 = convert_to_dict_garage(garage1)
my_json_garage = json.dumps(garage2, indent=4)
print(my_json_garage)

collectionar1 = Collectioner('Vadik', garage1)
collectionar2 = convert_to_dict_collectioner(collectionar1)
my_json_collectionar = json.dumps(collectionar2, indent=4)

# __DUMP

with open ('my_json_car.txt','w') as file:
    json.dump(convert_to_dict_car(car1),file,indent=4)
with open('my_json_garage','w') as file:
    json.dump(convert_to_dict_garage(garage1),file,indent=4)
with open('my_json_collectionar','w') as file:
    json.dump(convert_to_dict_collectioner(collectionar1),file,indent=4)

# __LOADS


my_json_loads_car = json.loads(my_json_car1,object_hook=dict_to_object_car)
print(my_json_loads_car)

my_json_loads_garage = json.loads(my_json_garage,object_hook= dict_to_object_car)
print(my_json_garage)

my_json_loads_collectionar =json.loads(my_json_collectionar, object_hook= dict_to_object_car)
print(my_json_loads_collectionar)

# _LOAD

with open ('my_json_car.txt','r') as file:
    my_car = json.load(file)
print(my_car)

with open('my_json_garage','r') as file:
    my_garage = json.load(file)
print(my_garage)
with open('my_json_garage', 'r') as file:
        my_collectionar = json.load(file)
print(my_collectionar)

# ___________PICKLE_____________

DUMPS__DUMP
my_pickle_car1 = pickle.dumps(car1)
print(my_pickle_car1)
with open("my_pickle_car2.txt", "wb") as file:
    pickle.dump(Car, file)

my_pickle_garage = pickle.dumps(garage1)
print(my_pickle_garage)
with open("my_pickle_garage.txt", "wb") as file:
#     pickle.dump(Garage, file)

my_pickle_collctionar = pickle.dumps(collectionar1)
print(my_pickle_collctionar)
with open("my_pickle_collectioare.txt", "wb") as file:
    pickle.dump(Collectioner, file)

# LOAD__LOADS
my_pickle_car1_loads = pickle.loads(my_pickle_car1)
print(my_pickle_car1_load)
with open("my_pickle_car2.txt", "rb") as file:
    restore_obj = pickle.load(file)
    print(restore_obj)

my_picke_garage_loads = pickle.loads(my_pickle_garage)
print(my_picke_garage_loads)
with open("my_pickle_garage.txt", "rb") as file:
    restore_obj = pickle.load(file)
    print(restore_obj)

my_pickle_collectionare_loads = pickle.loads(my_pickle_collctionar)
print(my_pickle_collectionare_loads)
with open("my_pickle_collectioare.txt", "rb") as file:
    restore_obj = pickle.load(file)
    print(restore_obj)

#_____YAML____
#_DUMP
yaml = YAML(typ='unsafe')

with open("car1.yaml", "w") as file:
    yaml.dump(car1, file)
with open("garage1.yaml",'w') as file:
    yaml.dump(garage1,file)
with open('collectionar1.yaml','w') as file:
    yaml.dump(collectionar1,file)

#_LOAD
with open("car1.yaml", "r") as file:
        yaml_car = yaml.load(file)
print(yaml_car)
with open("garage1.yaml", "r") as file:
    yaml_garage = yaml.load(file)
print(yaml_garage)
with open("collectionar1.yaml", "r") as file:
    yaml_collectionar = yaml.load(file)
print(yaml_collectionar)