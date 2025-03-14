import unittest
from src.ship import Ship


class TestShipInitialization(unittest.TestCase):

    def setUp(self):
        pass

    def test_creation(self):
        ship1 = Ship("Rotterdam", 7)
        self.assertIsInstance(ship1, Ship)

    def test_initialization(self):
        ship1 = Ship("Rotterdam", 7)
        self.assertEqual(ship1.destination, "Rotterdam")
        self.assertEqual(ship1.voyage_duration, 7)

    def test_calculate_fuel(self):
        ship1 = Ship("Rotterdam", 7)
        self.assertEqual(ship1.calculate_fuel(), 700)
        ship2 = Ship("Singapore", 5)
        self.assertEqual(ship2.calculate_fuel(), 500)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
