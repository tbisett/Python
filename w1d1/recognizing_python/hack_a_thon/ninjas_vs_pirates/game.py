from classes.ninja import Ninja
from classes.pirate import Pirate

class Die(object):
    def __init__(self, sides = 6):
        self.sides = sides

    def roll(self):
        return randint(1, self.sides)












michelangelo = Ninja("Michelanglo")
jack_sparrow = Pirate("Jack Sparrow")
michelangelo.attack(jack_sparrow)
jack_sparrow.show_stats()



