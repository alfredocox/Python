#! /usr/bin/env python
#class07.py

class House:
    number_of_houses = 0
    
    def __init__(self, number = "not defined"):
        self.number = number
        House._add_house()

    def __del__(self):
        if House: 
            House._remove_house()
    @classmethod
    def _remove_house(cls):
        cls.number_of_houses -=1

    @classmethod
    def _add_house(cls):
        cls.number_of_houses+=1

    @classmethod
    def house_count(cls):
        return cls.number_of_houses

my_house = House(20)

print("My house is number ", my_house.number)
print("The number of houses: ",House.house_count())

del my_house
print("The number of houses: ", House.house_count())

your_house = House()
print("/nYour house is number ", your_house.number)
print("The number of houses: ", House.house_count())

print("/nThat's all folks!!")