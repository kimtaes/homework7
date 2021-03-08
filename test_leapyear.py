import unittest
import leapyear

class TestCase(unittest.TestCase):
    def test1(self):
        # 1997: a year not divisible by 4, 100 or 400
        self.assertEqual(leapyear.IsLeapYear(1997), 'NO')

        # 2012: divisible by 4 but not by 100 and 400
        self.assertEqual(leapyear.IsLeapYear(2012), 'YES')

        #1900: divisible by 4 and 100 but not by 400
        self.assertEqual(leapyear.IsLeapYear(1900), 'NO')

        
if __name__ == '__main__':
    unittest.main()
