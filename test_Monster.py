import unittest
from Monster import Monster


class TestMonster(unittest.TestCase):

    def setUp(self):
        self.monster = Monster("Goblin", 10, 100)

    def test_initialization(self):
        self.assertEqual(self.monster.name, "Goblin")
        self.assertEqual(self.monster.strength, 10)
        self.assertEqual(self.monster.health, 100)
        self.assertEqual(self.monster.lost_health, 0)

    def test_str_method(self):
        self.assertEqual(str(self.monster), "Monster Goblin has 10 strength and 100 health.")

    def test_take_damage(self):
        self.monster.take_damage(30)
        self.assertEqual(self.monster.health, 70)
        self.assertEqual(self.monster.lost_health, 30)

    def test_take_damage_exceeding_health(self):
        self.monster.take_damage(150)
        self.assertEqual(self.monster.health, 0)
        self.assertEqual(self.monster.lost_health, 100)

    def test_take_damage_exact_health(self):
        self.monster.take_damage(100)
        self.assertEqual(self.monster.health, 0)
        self.assertEqual(self.monster.lost_health, 100)

    def test_take_damage_zero(self):
        self.monster.take_damage(0)
        self.assertEqual(self.monster.health, 100)
        self.assertEqual(self.monster.lost_health, 0)

    def test_properties_are_read_only(self):
        with self.assertRaises(AttributeError):
            self.monster.name = "Orc"
        with self.assertRaises(AttributeError):
            self.monster.strength = 20
        with self.assertRaises(AttributeError):
            self.monster.health = 80
        with self.assertRaises(AttributeError):
            self.monster.lost_health = 10


if __name__ == "__main__":
    unittest.main()
