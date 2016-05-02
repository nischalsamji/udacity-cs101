import unittest
from seconds_in_a_week import days_in_a_week

class daysTest(unittest.TestCase):
    def testdays(self):
        self.assertEqual(days_in_a_week(), 604800)


if __name__ == '__main__':
    unittest.main()
