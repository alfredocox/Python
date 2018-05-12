from NewAnimalClass import newAnimal

class Cat(newAnimal):
    
    def __init__(self,name,eyecolor):
        super(Cat,self).__init__(name)
        self.eyecolor = eyecolor
    
    def get_eyecolor(self):
        return self.__eyecolor
    def set_eyecolor(self,newColor):
        self.__eyecolor=newColor
    
    eyecolor = property(get_eyecolor,set_eyecolor)

    def __str__(self):
        return "My name is "+self.get_name()

    def talk(self):
        """
        The Cat Talks!
        """
        print('{0} says, "Meow"'.format(self.name))