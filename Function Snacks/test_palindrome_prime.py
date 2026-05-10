import unittest
from palindrome_prime import is_palindrome_prime

class TestPalindromePrime(unittest.TestCase):

    def test_edge_cases(self):
        """Numbers less than 2 should be false."""
        self.assertFalse(is_palindrome_prime(0))
        self.assertFalse(is_palindrome_prime(1))
        self.assertFalse(is_palindrome_prime(-1))
    
    def test_prime_but_not_palindrome(self):
        """13 is prime but not a palindrome."""
        self.assertFalse(is_palindrome_prime(13))
    
    def test_palindrome_but_not_prime(self):
        """9 is a palindrome but not prime."""
        self.assertFalse(is_palindrome_prime(9))
    
    def test_is_both(self):
        """Check numbers that meet both criterial."""
        self.assertTrue(is_palindrome_prime(2))
        self.assertTrue(is_palindrome_prime(131))
    
if __name__ =="__main__":unittest.main()
        
        
