from Monster import Monster
from Player import Player
from Room import Room
import random


def initialize_player(name=None):
    if name is None:
        name = input("What is your name? ")
    player1 = Player(name, random.randint(40, 80))
    return player1

def initialize_rooms(room_config):
    rooms = []
    for i in range(len(room_config)): 
        rooms.append(Room(room_config[i]["desc"], Monster(room_config[i]["monster"], random.randint(40, 80), random.randint(20, 40))))
    return rooms

def print_results(player):
    print('---------------------------------------------')
    print("The game is over!")
    print(player)
    print("Thank you for playing Dungeon Master!")
    print("Good Bye!")

def run_game(nr_of_rooms):
    print("Welcome to the Dungeon")
    player = initialize_player()
    rooms_dict = {}
    for i in range(nr_of_rooms):
        desc = input("Description of the room: ")
        monster = input("Name of the monster: ")
        rooms_dict.update({i: {"desc": desc, "monster": monster}})
    rooms = initialize_rooms(rooms_dict)
    for room in rooms:
        while player.health != 0 and room.monster.health != 0:
            room.interact(player)
        if player.health == 0:
            print("Sorry - you died!")
            break
    print_results(player)

if __name__ == "__main__":
    run_game(5)
