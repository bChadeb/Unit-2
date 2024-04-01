from abc import ABC, abstractmethod
import csv
from pprint import pprint

class Cupcake(ABC):
    size = "normal"
    
    def __init__(self, name, price, flavor, frosting, filling):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []

    def add_sprinkles(self, *args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)

    @abstractmethod
    def calculate_price(self, quantity):
        return quantity * self.price 

class Mini(Cupcake):
    size = 'mini'
    
    def __init__(self, name, price, flavor, frosting):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = []

    def calculate_price(self, quantity):
        return quantity * self.price 

class Big(Cupcake):
    size = 'big'

    def calculate_price(self, quantity):
        return quantity * self.price

class Normal(Cupcake):
    size = 'normal'

    def calculate_price(self, quantity):
        return quantity * self.price

def read_csv(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            pprint(row)

def write_new_csv(file, cupcakes):
    with open(file, "w", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for cupcake in cupcakes:
            cupcake_dict = cupcake.__dict__
            cupcake_dict["sprinkles"] = ",".join(cupcake_dict["sprinkles"])  
            writer.writerow(cupcake_dict)

def add_cupcake(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        cupcake_dict = cupcake.__dict__
        cupcake_dict["sprinkles"] = ",".join(cupcake_dict["sprinkles"])  
        writer.writerow(cupcake_dict)

def get_cupcakes(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        reader = list(reader)
        return reader

def find_cupcake(file, name):
    for cupcake in get_cupcakes(file):
        if cupcake["name"] == name:
            return cupcake
    return None

def add_cupcake_dictionary(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(cupcake)


cupcake1 = Normal("Stars and Stripes", 2.99, "Vanilla", "Vanilla", "Chocolate")
cupcake1.add_sprinkles("Red", "White", "Blue")
cupcake2 = Mini("Oreo", .99, "Chocolate", "Cookies and Cream")
cupcake2.add_sprinkles("Oreo pieces")
cupcake3 = Big("Red Velvet", 3.99, "Red Velvet", "Cream Cheese", None)

cupcake_list = [cupcake1, cupcake2, cupcake3]

write_new_csv("cupcakes.csv", cupcake_list)
add_cupcake("cupcakes.csv", cupcake3)
read_csv("cupcakes.csv")
