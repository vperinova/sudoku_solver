from objekty import area, box, field

import unittest

class TestBox(unittest.TestCase):
    def test_odeber_poss_value(self):
        krabice = box.Box()
        krabice.odeber_poss_value(2)
        krabice.odeber_poss_value(4)
        krabice.odeber_poss_value(6)
        krabice.odeber_poss_value(8)
        krabice.odeber_poss_value(2)
        self.assertEqual(krabice.possible_values, [1,3,5,7,9])

    def test_zapis_hodnotu(self):
        krabice = box.Box()
        krabice.zapis_hodnotu(1)
        self.assertEqual(krabice.possible_values, [1])
        self.assertEqual(krabice.value, 1)
        krabice.zapis_hodnotu(3)
        self.assertNotEqual(krabice.value, 3)


if __name__ == '__main__':
    unittest.main()