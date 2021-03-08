import unittest
import leapyear

class TestCase(unittest.TestCase):
    def test1(self):
        # 1997: a year not divisible by 4, 100 or 400
        self.assertEqual(leapyear.IsLeapYear(1997), 'NO')

if __name__ == '__main__':
    unittest.main()
