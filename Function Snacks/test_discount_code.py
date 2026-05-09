import unittest

from discount_code import calculate_discount

class TestDiscountFunction(unittest.TestCase):

    def test_save10_discount(self):
        self.assertEqual(calculate_discount("cereal", 100, "SAVE10"), 90.0)
        
    def test_halfoff_discount(self):
        self.assertEqual(calculate_discount("cereal", 100, "HALFOFF"), 50.0)
        
    def test_invalid_code(self):
       self.assertEqual(calculate_discount("cereal", 100, "FAKECODE"), 100.0)
       
    def test_case_sensitivity(self):
        self.assertEqual(calculate_discount("cereal", 100, "halfoff"), 50.0)
        
if __name__ =="__main__":unittest.main()
    

