class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100
        self.ability = 35

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        ninja.health -= self.strength
        return self

    def heavy_attack(self, ninja):
        ninja.health -= (self.strength * 1.5)
        return self
    
    def ability_strike(self, ninja):
        ninja.health -= self.ability
        self.speed += 5
        return self

    def absorb_health(self, ninja):
        self.health += ninja.strength
        return self
    