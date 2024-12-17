import unittest
from Player import Player


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("Hero", 20)

    def test_initialization(self):
        self.assertEqual(self.player.name, "Hero")
        self.assertEqual(self.player.strength, 20)
        self.assertEqual(self.player.health, 100)

    def test_str_method(self):
        self.assertEqual(str(self.player), "Player Hero has 20 strength and 100 health.")

    def test_take_damage(self):
        self.player.take_damage(30)
        self.assertEqual(self.player.health, 70)

    def test_take_damage_exceeding_health(self):
        self.player.take_damage(150)
        self.assertEqual(self.player.health, 0)

    def test_take_damage_zero(self):
        self.player.take_damage(0)
        self.assertEqual(self.player.health, 100)

    def test_regain_health(self):
        self.player.take_damage(50)
        self.player.regain_health(30)
        self.assertEqual(self.player.health, 80)

    def test_regain_health_exceeding_max(self):
        self.player.regain_health(10)
        self.assertEqual(self.player.health, 100)
        self.player.take_damage(20)
        self.player.regain_health(50)
        self.assertEqual(self.player.health, 100)

    def test_regain_health_with_float(self):
        self.player.take_damage(50)
        self.player.regain_health(30.8)
        self.assertEqual(self.player.health, 80)

    def test_properties_are_read_only(self):
        with self.assertRaises(AttributeError):
            self.player.name = "Villain"
        with self.assertRaises(AttributeError):
            self.player.strength = 25
        with self.assertRaises(AttributeError):
            self.player.health = 90


if __name__ == "__main__":
    unittest.main()
