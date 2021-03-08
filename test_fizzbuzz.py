import fizzbuzz
import unittest

class TestCase(unittest.TestCase):
    def test1(self):
        for num in range (1,100):
            if num % 3 ==0:
                self.assertEqual(fizzbuzz.fizzbuzz(num), 'Fizz')
            elif num % 5 ==0:
                self.assertEqual(fizzbuzz.fizzbuzz(num), 'Buzz')
            elif num % 3 == 0 and num % 5 == 0:
                self.assertEqual(fizzbuzz.fizzbuzz(num),'FizzBuzz')
            else:
                self.assertEqual(fizzbuzz.fizzbuzz(num), num)


if __name__ == '__main__':
    unittest.main()