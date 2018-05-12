#! /usr/bin/env python
# class02.py
class House: 
    pass

my_house=House()
my_house.number =40
my_house.room  =8
my_house.garden = 1

print ("My house is number", my_house.number)
print ("It has", my_house.room, " rooms.")
print ("It","has" if my_house.garden else "does not have", "a garden")

your_house = House()
print ("your house is number", your_house.number)