class Auto:
    def __init__(self, brand, age, cоlor, mark, weight):
        self.brand = brand
        self.age = age
        self.cоlor = cоlor
        self.mark = mark
        self.weight = weight

    def move_car(self):
        print('move')

    def stop_car(self):
        print('stop!')

    def birthday(self):
        self.age += 1

my_cars = Auto("Lexus", 7, 'black', 'CT200h', 1450)

print(my_cars.brand)
print(my_cars.age)
print(my_cars.mark)

