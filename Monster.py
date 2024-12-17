import string


class Monster:
    def __init__(self, name, strength, health):
        self.name = name
        self.strength = strength
        self.health = health
        
    def __str__(self):
        return "Monster " + self.name + " hast strength " + string(self.strength) + " and health " + string(self.strength) + ". "
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0