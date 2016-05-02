from week1.src import seconds_in_a_week as sec
import unittest
import sys

sys.path.append('./')


class daysTest(unittest.TestCase):
    def testdays(self):
        self.assertEqual(sec.days_in_a_week(), 604800)


if __name__ == '__main__':
    unittest.main()
