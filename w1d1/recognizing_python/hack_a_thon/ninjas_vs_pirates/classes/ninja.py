class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
        self.ability = 35
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        pirate.health -= self.strength
        return self

    def heavy_attack(self, pirate):
        pirate.health -= (self.strength * 1.5)
        return self
    
    def ability_strike(self, pirate):
        pirate.health -= self.ability
        self.speed += 5
        return self

    def absorb_health(self, pirate):
        self.health += pirate.strength
        return self