import unittest
from src.char_struct.characteristics import Characteristic


class TestCharacteristic(unittest.TestCase):
    def test_characteristic_creation(self):
        bonus = [
            [1, 74, 0], [75, 89, 5], [90, 94, 10],
            [95, 97, 15], [98,99,20], [100,100,25],
            [101,101,30], [102,102,35]
            ]
        race_bonus = 10
        characteristic = Characteristic(95,race_bonus, bonus)
        self.assertIsInstance(characteristic, Characteristic)
        self.assertIsInstance(characteristic.roll, int)
        self.assertEqual(characteristic.roll, 95)
        self.assertIsInstance(characteristic.race_bonus, int)
        self.assertEqual(characteristic.race_bonus, 10)
        self.assertIsInstance(characteristic.roll_bonuses(), int)
        self.assertEqual(characteristic.roll_bonuses(), 15)
        self.assertIsInstance(characteristic.total_bonus(), int)
        self.assertEqual(characteristic.total_bonus(), 25)


if __name__ == "__main__":
    unittest.main()