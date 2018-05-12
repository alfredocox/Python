#! usr/bin/env python
# AnimalClass01.py

class Animal:


    def __init__(self,name,age):
        self.name=name
        self.age = age
    
    def __eq__(self,a):
        return self.name==a.name and self.age == a.age

tiger = Animal("Charlie",20)
lion = Animal("Charlie",20)

print (tiger.__eq__(lion))