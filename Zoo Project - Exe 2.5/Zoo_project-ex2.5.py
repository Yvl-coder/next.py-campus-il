class Animal:
    """
    This class used to represent an animal.
    """
    zoo_name = "Hayaton"
    
    def __init__(self, name, hunger=0):
        """
        This method sets initial values.
        :param name: the animal name
        :param hunger: how much the animal hunger
        :type name: str
        :type hunger: int
        :return: None
        :rtype: None
        """
        self._name = name
        self._hunger = hunger
    
    def get_name(self): 
        """
        This method returns the animal name.
        :return: the animal name
        :rtype: str
        """
        return self._name
    
    def is_hungry(self):
        """
        This method returns if the animal is hungry.
        :return: if the animal is hungry (hunger is bigger than zero)
        :rtype: bool
        """
        return self._hunger > 0 
    
    def feed(self):
        """
        This method minus by 1 from hunger.
        :return: None
        :rtype: None
        """
        self._hunger -= 1

    def talk(self):
        """
        This method will be implemented for each animal type.
        :return: None
        :rtype: None
        """
        pass

   
class Dog(Animal):
    """
    This class used to represent a dog.
    """
    
    def talk(self):
        """
        This method will display what the dog say.
        :return: None
        :rtype: None
        """
        print("woof woof")

    def fetch_stick(self):
        """
        This method is especially for the dog.
        :return: None
        :rtype: None
        """
        print("There you go, sir!")

class Cat(Animal):
    """
    This class used to represent a cat.
    """
    
    def talk(self):
        """
        This method will display what the cat say.
        :return: None
        :rtype: None
        """
        print("meow")

    def chase_laser(self):
        """
        This method is especially for the cat.
        :return: None
        :rtype: None
        """
        print("Meeeeow")   

class Skunk(Animal):
    """
    This class used to represent a skunk.
    """
    
    def __init__(self, name, hunger=0, stink_count=6):
        """
        This method sets initial values.
        :param name: the animal name
        :param hunger: how much the animal hunger
        :param stink_count: how much the skunk stink
        :type name: str
        :type hunger: int
        :type stink_count: int
        :return: None
        :rtype: None
        """
        super().__init__(name, hunger)
        self._stink_count = stink_count
    
    def talk(self):
        """
        This method will display what the skunk say.
        :return: None
        :rtype: None
        """
        print("tsssss")
    
    def stink(self):
        """
        This method is especially for the skunk.
        :return: None
        :rtype: None
        """
        print("Dear lord!")

class Unicorn(Animal):
    """
    This class used to represent an unicorn.
    """
    
    def talk(self):
        """
        This method will display what the unicorn say.
        :return: None
        :rtype: None
        """
        print("Good day, darling")
    
    def sing(self):
        """
        This method is especially for the unicorn.
        :return: None
        :rtype: None
        """
        print("I’m not your toy...")

class Dragon(Animal):
    """
    This class used to represent a dragon.
    """
    
    def __init__(self, name, hunger=0, color="Green"):
        """
        This method sets initial values.
        :param name: the animal name
        :param hunger: how much the animal hunger
        :param color: the dragon color
        :type name: str
        :type hunger: int
        :type color: str
        :return: None
        :rtype: None
        """
        super().__init__(name, hunger)
        self._color = color

    def talk(self):
        """
        This method will display what the dragon say.
        :return: None
        :rtype: None
        """
        print("Raaaawr")
    
    def breath_fire(self):
        """
        This method is especially for the dragon.
        :return: None
        :rtype: None
        """
        print("$@#$#@$")
    
def main():
    zoo_lst = [Dog('Brownie', 10), Cat('Zelda', 3), Skunk('Stinky'), Unicorn('Keith', 7), Dragon('Lizzy', 1450), Dog('Doggo', 80), Cat('Kitty', 80), Skunk('Stinky Jr.', 80), Unicorn('Clair', 80), Dragon('McFly', 80)] 
    
    for animal in zoo_lst:
        if animal.is_hungry():
            print(animal.__class__.__name__, animal.get_name())
            while animal.is_hungry():
                    animal.feed()
        animal.talk()
        
        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()

    print(Animal.zoo_name)

if __name__ == "__main__":
    main()