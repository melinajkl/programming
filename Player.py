from random import uniform
import string

class Player:
    def __init__(self, name, strength):
        self.name = name
        self.health = 100
        self.strength = strength
        
    def __str__(self):
        return "Player" + self.name + " has " + string(self.strength) + " strength and " + string(self.health) + " health. "
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
    
    def regain_health(self, health_regain):
        self.health += health_regain
        if (self.health > 100): 
            self.health = 100