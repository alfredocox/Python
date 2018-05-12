#! /usr/bin/env python
#class03.py

class House:
    def __init__(self, number ="not defined",rooms ="not defined",garden ="not defined"):
        self.number=number
        self.rooms=rooms
        self.garden=garden

my_house = House(20,1,0)

print("My house is number ", my_house.number)
print ("It has", my_house.rooms," rooms.")
print("it ","has " if my_house.garden else "does not have", "a garden.")