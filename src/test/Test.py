import unittest

def fizzbuzz(num):
    if num % 15 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return 'Other'

class FizzBuzzTest(unittest.TestCase):
    def test_fizzbuzz(self):
        self.assertEqual('Fizz', fizzbuzz(3))
        self.assertEqual('Buzz', fizzbuzz(5))
        self.assertEqual('FizzBuzz', fizzbuzz(15))
        self.assertEqual('Other', fizzbuzz(2))

if __name__ == "__main__":
    unittest.main()