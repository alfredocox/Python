class Animal:
    """
    Base Class for an animal that has a name
    """
    def __init__(self,name="none"):
        """
        Defines instance of Animal

        Argument:
        name: name of the animal (string)
        """
        self.name=name

    def __eq__(self,a):
        return self.name == a.name

    def __str__(self):
        """
        What is printed when name of an instance object is
        """    
        return self.name

    def talk(self):
        """
        animal speaks
        """
        print ("General Animal Sound")

    def get_name(self):
        return self.name

    def set_name(self,newName):
        """
        Sets animal's name 

        Argument:
        newName: new name of animal (string)
        """
        self.name=newName
