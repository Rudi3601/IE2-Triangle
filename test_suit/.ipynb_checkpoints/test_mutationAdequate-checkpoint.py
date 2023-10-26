import unittest
from isTriangle import Triangle

class MutationTest(unittest.TestCase):
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
        
    def test_invalid_triangle3(self):
        actual = Triangle.classify(5, 5, 15)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
    def test_invalid_triangle4(self):
        actual = Triangle.classify(5, 15, 5)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
    def test_invalid_triangle5(self):
        actual = Triangle.classify(15, 5, 5)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
    def test_invalid_triangle6(self):
        actual = Triangle.classify(5, 15, 8)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
    def test_invalid_triangle7(self):
        actual = Triangle.classify(8, 5, 15)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
    def test_invalid_triangle8(self):
        actual = Triangle.classify(8, 15, 5)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
    def test_invalid_triangle9(self):
        actual = Triangle.classify(15, 5, 8)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
    def test_invalid_triangle10(self):
        actual = Triangle.classify(15, 8, 5)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
    def test_all_sides_zero(self):
        actual = Triangle.classify(0, 0, 0)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
    def test_edge_case1(self):
        actual = Triangle.classify(0, 1, 2)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
    def test_edge_case2(self):
        actual = Triangle.classify(0, 1, 0)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
    def test_edge_case3(self):
        actual = Triangle.classify(10, 5, 5)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
    def test_edge_case4(self):
        actual = Triangle.classify(5, 10, 5)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
    def test_edge_case5(self):
        actual = Triangle.classify(5, 5, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    
    def test_edge_case6(self):
        actual = Triangle.classify(5, 2, 3)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
    def test_edge_case7(self):
        actual = Triangle.classify(0, 0, 2)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
    def test_edge_case8(self):
        actual = Triangle.classify(1, 0, 0)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
    def test_edge_case9(self):
        actual = Triangle.classify(1, 2, 0)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
    def test_edge_case10(self):
        actual = Triangle.classify(2, 5, 3)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
    def test_edge_case11(self):
        actual = Triangle.classify(2, 3, 5)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
        

if __name__ == '__main__':
    unittest.main()