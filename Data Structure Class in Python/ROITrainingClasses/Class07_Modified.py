#! /usr/bin/env python
#class07.py

class House:
    number_of_houses = 0
    
    def __init__(self, number ="not defined",rooms ="not defined",garden ="not defined"):
        self.number=number
        self.rooms=rooms
        self.garden=garden
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

    def __eq__(self,other):        
        if type(other) == House:
           return self.rooms==other.rooms and self.garden == other.garden
        else: 
            return "obj parameter ",other," is not House class"
        
my_house = House(20,2,1)
your_house = House(21,2,1)

print ("my_house and your_house are ",my_house.__eq__(your_house))