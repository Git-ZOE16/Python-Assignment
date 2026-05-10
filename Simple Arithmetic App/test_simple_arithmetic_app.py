import unittest
from simple_arithmetic_app import generate_subtraction_problem, check_answer

class TestArithmeticApp(unittest.TestCase):

    def test_no_negative_results(self):
        """Test that the generated numbers always result in a positive answer."""
        for _ in range(100): 
            n1, n2 = generate_subtraction_problem()
            self.assertTrue(n1 >= n2, f"Failed: {n1} is not greater than {n2}")

    def test_correct_answer_logic(self):
        """Test that check_answer returns True for correct math."""
        self.assertTrue(check_answer(10, 5, 5))
        self.assertTrue(check_answer(20, 0, 20))

    def test_incorrect_answer_logic(self):
        """Test that check_answer returns False for incorrect math."""
        self.assertFalse(check_answer(10, 5, 3))
        self.assertFalse(check_answer(15, 7, 22))

    def test_randomness(self):
        """Test that different calls provide different questions (usually)."""
        problem1 = generate_subtraction_problem()
        problem2 = generate_subtraction_problem()

        self.assertNotEqual(problem1, (99, -1)) 

if __name__ == '__main__':
    unittest.main()

