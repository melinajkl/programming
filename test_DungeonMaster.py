import unittest
from unittest.mock import patch
from dungeon.Player import Player
from dungeon.DungeonMaster import initialize_player, initialize_rooms, print_results


class TestDungeonMaster(unittest.TestCase):

    @patch("random.randint", return_value=50)
    def test_initialize_player(self, mock_randint):
        player = initialize_player("Hero")
        self.assertEqual(player.name, "Hero")
        self.assertEqual(player.strength, 50)
        self.assertEqual(player.health, 100)

    @patch("random.randint", side_effect=[30, 60, 40, 80])
    def test_initialize_rooms(self, mock_randint):
        rooms_config = {
            0: {"desc": "Dark Cave", "monster": "Goblin"},
            1: {"desc": "Bright Hall", "monster": "Orc"}
        }
        rooms = initialize_rooms(rooms_config)

        self.assertEqual(len(rooms), 2)
        self.assertEqual(str(rooms[0]), "Dark Cave")
        self.assertEqual(rooms[0].monster.name, "Goblin")
        self.assertEqual(rooms[0].monster.strength, 30)
        self.assertEqual(rooms[0].monster.health, 60)

        self.assertEqual(str(rooms[1]), "Bright Hall")
        self.assertEqual(rooms[1].monster.name, "Orc")
        self.assertEqual(rooms[1].monster.strength, 40)
        self.assertEqual(rooms[1].monster.health, 80)

    @patch("builtins.print")
    def test_print_results(self, mock_print):
        player = Player("Hero", 50)
        print_results(player)

        mock_print.assert_any_call("---------------------------------------------")
        mock_print.assert_any_call("The game is over!")
        mock_print.assert_any_call(player)
        mock_print.assert_any_call("Thank you for playing Dungeon Master!")
        mock_print.assert_any_call("Good Bye!")

    def test_run_game(self):
        player = Player("Hero", 50)

        room_config = {
            0: {"desc": "Dark Cave", "monster": "Goblin"},
            1: {"desc": "Bright Hall", "monster": "Orc"}
        }
        dungeon = initialize_rooms(room_config)

        # simulate game
        for room in dungeon:
            if player.health <= 0:
                break
            print(f"Entering room: {room}")
            while player.health > 0 and room.monster.health > 0:
                # Player always fights
                room.fight_round(player)

        # check results
        self.assertGreater(player.health, 0, "Player should survive the dungeon if monsters are defeated.")
        self.assertTrue(all(m.health == 0 for m in [room.monster for room in dungeon]),
                        "All monsters should be defeated.")


if __name__ == "__main__":
    unittest.main()
