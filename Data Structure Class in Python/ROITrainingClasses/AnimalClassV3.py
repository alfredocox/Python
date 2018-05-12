from AnimalClassV2 import Animal

class Cat(Animal): 
    """
    Cat a subclass of Animal
    """

    number_of_cats = 0

    def __init__(self,name,eyeColor):
        """
        Creates a cat isntance
        """

        Animal.__init__(self,name)
        self.eyeColor=eyeColor
        Cat.number_of_cats+=1

    def __del__(self):
        if Cat:
            Cat.number_of_cats-=1
    
    def talk(self):
        """
        Cat speaks (Overwrite of Animal talk method)
        """

        print("Meow!!!")  