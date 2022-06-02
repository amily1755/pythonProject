import unittest

from die import Die
class MyTestCase(unittest.TestCase):
    def test_something(self):
        die = Die(10)
        self.assertEqual(10, die.num_sides)

if __name__ == '__main__':
    unittest.main()
