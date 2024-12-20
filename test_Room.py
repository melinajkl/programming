import unittest
from unittest.mock import patch
from dungeon.Monster import Monster
from dungeon.Room import Room
from dungeon.Player import Player


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.monster = Monster("Goblin", 15, 50)
        self.player = Player("Hero", 20)
        self.room = Room("Dark Cave", self.monster)

    def test_initialization(self):
        self.assertEqual(str(self.room), "Dark Cave")
        self.assertEqual(self.room.description, "Dark Cave")
        self.assertEqual(self.room.monster, self.monster)

    def test_fight_round_monster_alive(self):
        initial_player_health = self.player.health
        initial_monster_health = self.monster.health

        self.room.fight_round(self.player)

        self.assertEqual(self.player.health, initial_player_health - self.monster.strength)
        self.assertEqual(self.monster.health, initial_monster_health - self.player.strength)

    def test_fight_round_monster_dies(self):
        self.monster = Monster("Goblin", 15, 20)
        self.room = Room("Dark Cave", self.monster)

        self.room.fight_round(self.player)

        self.assertEqual(self.monster.health, 0)
        self.assertTrue(self.player.health > 0)
        # monster looses 20 health, player looses 15 health, player regains 20/2 health -> 95 health
        self.assertEqual(self.player.health, 95)

    def test_fight_round_player_dies(self):
        self.player = Player("Hero", 20)
        self.player.take_damage(100)  # Player starts with 0 health

        self.room.fight_round(self.player)

        self.assertEqual(self.player.health, 0)
        self.assertTrue(self.monster.health > 0)

    def test_interact_run(self):
        with unittest.mock.patch("builtins.input", return_value="r"):
            self.room.interact(self.player)

        self.assertEqual(self.player.health, 90)

    def test_interact_fight(self):
        self.monster = Monster("Goblin", 15, 30)
        self.room = Room("Dark Cave", self.monster)

        with unittest.mock.patch("builtins.input", side_effect=["f", "r"]):
            self.room.interact(self.player)

        self.assertTrue(self.player.health < 100)
        self.assertTrue(self.monster.health < 30)
        self.assertEqual(self.player.health, 75)


if __name__ == "__main__":
    unittest.main()
