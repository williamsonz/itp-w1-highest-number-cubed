import unittest

from highest_number_cubed import highest_number_cubed


class TestHighestNumberCubed(unittest.TestCase):

    def test_three(self):
        self.assertEqual(highest_number_cubed(30), 3)

    def test_two(self):
        self.assertEqual(highest_number_cubed(12), 2)

    def test_one(self):
        self.assertEqual(highest_number_cubed(3), 1)

    def test_big(self):
        self.assertEqual(highest_number_cubed(12000), 22)
