import unittest
from isTriangle import Triangle

class DecisionTest(unittest.TestCase):
    def test_equilateral_triangle(self):
        actual = Triangle.classify(10, 10, 10)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)
        
    def test_isosceles_triangle1(self):
        actual = Triangle.classify(10, 10, 13)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)
        
    def test_isosceles_triangle2(self):
        actual = Triangle.classify(13, 10, 10)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)
        
    def test_isosceles_triangle3(self):
        actual = Triangle.classify(10, 13, 10)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)
        
    def test_scalene_triangle(self):
        actual = Triangle.classify(3, 4, 5)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)
        
    def test_invalid_triangle1(self):
        actual = Triangle.classify(-3, 4, 5)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
    def test_invalid_triangle2(self):
        actual = Triangle.classify(5, 8, 15)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
        

if __name__ == '__main__':
    unittest.main()