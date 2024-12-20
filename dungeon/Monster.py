import string

class Monster:
    def __init__(self, name, strength, health):
        self.__name = name
        self.__strength = strength
        self.__health = health
        self._lost_health = 0
        self.max_health = health
    
    @property
    def lost_health(self):
        return self._lost_health
    
    @property
    def name(self):
        return self.__name
    
    @property
    def strength(self):
        return self.__strength
    
    @property
    def health(self):
        return self.__health
        
    def __str__(self):
        return f"Monster {self.__name} has {self.__strength} strength and {self.__health} health."
    
    def take_damage(self, damage):
        self.__health -= damage
        self._lost_health += damage
        if self.__health < 0:
            self.__health = 0
            self._lost_health = self.max_health