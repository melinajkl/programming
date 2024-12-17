from random import uniform

class Player:
    def __init__(self, name, strength):
        self._name = name
        self._health = 100
        self._strength = float(strength)
        
    def name(self):
        return self._name
    
    def health(self):
        return self._health
    
    def strength(self):
        return self._strength
        
    def __str__(self):
        return f"Player {self._name} has {self._strength} strength and {self._health} health."
    
    def take_damage(self, damage):
        self._health -= damage
        if self._health < 0:
            self._health = 0
    
    def regain_health(self, health_regain):
        self._health += health_regain
        if self._health > 100:
            self._health = 100
