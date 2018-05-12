#! /usr/bin/env python
#class01.py

class House:
    pass

my_house = House()
my_house.number = 40
my_house.rooms = 8
my_house.garden = 1

print("My house is number ", my_house.number)
print ("It has", my_house.rooms," rooms.")
print("it ","has " if my_house.garden else "does not have", "a garden.")