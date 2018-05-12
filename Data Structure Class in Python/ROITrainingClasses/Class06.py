#! /usr/bin/env python
#class06.py

class House:
    number_of_houses = 0
    def __init__(self, number ="not defined"):
        self.number=number
        House.number_of_houses+=1

    def __del__(self):
        if House:
            House.number_of_houses-=1

my_house = House(20)

print ("My house is number", my_house.number)
print ("the number of houses: ", my_house.number_of_houses)

del my_house

print("The number of houses", House.number_of_houses)

your_house = House()
print ("/nYour house is number ", your_house.number)
print ("The number of houses: ", House.number_of_houses)

print("\nThat's all folks!")

    

