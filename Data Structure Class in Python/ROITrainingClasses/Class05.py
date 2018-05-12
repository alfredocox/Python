#! /usr/bin/env python
#class05.py

class House:
    number_of_houses = 0
    def __init__(self, number ="not defined",rooms ="not defined",garden ="not defined"):
        self.number=number
        self.rooms=rooms
        self.garden=garden
        House.number_of_houses+=1

my_house = House(20,1,0)

print("My house is number ", my_house.number)
print ("The number of houses: ",my_house.number_of_houses)

your_house = House()

print ("\nYour house is number ", my_house.number)
print("The number of houses: ", House.number_of_houses)

