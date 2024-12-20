class Room:
    def __init__(self, description, monster):
        self.__description = description
        self.__monster = monster
    
    @property
    def description(self):
        return self.__description
    
    @property
    def monster(self):
        return self.__monster
    
    def __str__(self):
        return self.__description
    
    def fight_round(self, player):
        print(f"The monster hits you with strength {self.__monster.strength}")
        player.take_damage(self.__monster.strength)
        print(player)
        print(f"You hit the monster with strength {player.strength}")
        self.__monster.take_damage(player.strength)
        print(self.monster)
        if self.__monster.health == 0:
            print("The monster is dead")
            player.regain_health(self.__monster.max_health // 2)
            print(f"{player.name}, you regained health: {self.__monster.max_health // 2}")
        if player.health == 0:
            print("You lost the fight")
            
    def interact(self, player):
        print(f"Welcome to the {self.description}. The monster {self.__monster.name} appears!")
        while self.__monster.health != 0 and player.health != 0:
            print("Would you like to run (r) or fight (f)?")
            choice = input().strip().lower()
            if choice == 'r':
                print("You chose RUN!")
                player.take_damage(10)
                print("You sprint out of the room and take 10 damage!")
                print(player)
                break
            elif choice == 'f':
                print("You chose FIGHT!")
                self.fight_round(player)
            else:
                print("Invalid choice. Please enter 'r' to run or 'f' to fight.")
