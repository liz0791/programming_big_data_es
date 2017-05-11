#test to see if the 10 functions are working corectly 
from calculator import add, subtract, multiply, division, exponent, factorial_, sqrt, sine, cosine, tangent    
    
import unittest


class Mytestt(unittest.TestCase):
    def testAdd(self):
        self.assertEqual(add(2.0,2.0), 4.0)
        self.assertEqual(add(5.0,3.0), 8.0)
        self.assertEqual(add(4.0,0.0), 4.0)
        
    def testSubtract(self):
        self.assertEqual(subtract(2.0,2.0), 0.0)
        self.assertEqual(subtract(5.0,3.0), 2.0)
        self.assertEqual(subtract(4,0), 4)
        
    def testMultiply(self):
        self.assertEqual(multiply(2.0,2.0), 4.0)
        self.assertEqual(multiply(5.0,3.0), 15.0)
        self.assertEqual(multiply(4.0,0.0), 0.0)   
                  
    def testDivision(self):
        self.assertEqual(division(2.0,2.0), 1.0)
        self.assertEqual(division(5.0,2.0), 2.5)
        self.assertEqual(division(4,0), "You can't divide by zero")  
        
    def testExponent(self):
        self.assertEqual(exponent(2.0,2.0), 4.0)
        self.assertEqual(exponent(5.0,3.0), 125.0)
        self.assertEqual(exponent(4.0,0.0), 1.0)   
    
    def testFactorial_(self):
        self.assertEqual(factorial_(3.5), "Factorial only accepts integral values")
        self.assertEqual(factorial_(6.0), 720.0)
        self.assertEqual(factorial_(12.0), 479001600.0)
        
    def testSqrt(self):
        self.assertEqual(sqrt(-4.0), "The square root of a negative is undefined over the Reals")
        self.assertEqual(sqrt(25.0), 5.0)
        self.assertEqual(sqrt(345.0), 18.57417562100671)
        
    def testSine(self):
        self.assertEqual(sine(90.0), 0.8939966636005579)
        self.assertEqual(sine(45.0), 0.8509035245341184)
        self.assertEqual(sine(180.0), -0.8011526357338306)
        
    def testCosine(self):
        self.assertEqual(cosine(90.0), -0.4480736161291701)
        self.assertEqual(cosine(45.0), 0.5253219888177297)
        self.assertEqual(cosine(180.0), -0.5984600690578581)
        
    def testTangent(self):
        self.assertEqual(tangent(90.0),-1.995200412208242)
        self.assertEqual(tangent(45.0), 1.6197751905438615)
        self.assertEqual(tangent(180.0), 1.3386902103511547)
       
if __name__ =='__main__':
    unittest.main()
