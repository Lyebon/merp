import unittest
from character.characteristics import Caracteristic
from builder import dice



class TestCharacteristic(unittest.TestCase):
    def test_characteristic_creation(self):
        characteristic = Caracteristic(dice(100), race_bonus=10)

        self.assertIsInstance(characteristic, Caracteristic)
        print(repr(characteristic))


if __name__ == "__main__":
    unittest.main()


if __name__ == "__main__":
    unittest.main()