# practic_python

Университетский курс по Питону. Задачи, которые могут быть полезны на собеседовании


+ [Calculator complex](#calculator-complex)
+ [Test calculator complex](#test-calculator-complex)

# Calculator

## Calculator complex

Реализация калькулятора комплексных чисел

```python

def Take_Rational_Part(x1):
    # Function return rational part from complex
    return x1.real


def Take_Imaginary_Part(x1):
    # Function return imaginary part
    return x1.imag


def Addition(x1, x2):
    # Function add two complex numbers
    result = x1 + x2
    return result
    

def Subtraction(x1, x2):
    # Function add two complex numbers
    result = x1 - x2
    return result
    

def Multiply(x1, x2):
    # Function multiply two complex numbers
    result = x1 * x2
    return result


def Division(x1, x2):
    result = x1 / x2 
    return result
```

# Test

## Test calculator complex

Тест система калькулятора

```python

import unittest


class TestComplex(unittest.TestCase):
    
    def test_equal(self):
        first = Complex(2, 5)
        second = Complex(2, 5)
        self.assertEqual(first, second)
        
    def test_equal_rtn(self):
        first = Complex(2, 6)
        second = Complex(2, 5)
        third = Complex(3, 1)
        self.assertEqual(Take_Rational_Part(first), Take_Rational_Part(second))      
        self.assertNotEqual(Take_Imaginary_Part(first), Take_Imaginary_Part(third))  
         
    def test_equal_img(self):
        first = Complex(2, 6)
        second = Complex(2, 5)
        third = Complex(3, 1)
        self.assertNotEqual(Take_Imaginary_Part(first), Take_Imaginary_Part(second))   
        self.assertEqual(Take_Imaginary_Part(first), Take_Imaginary_Part(third)
        
    def test_addition(self):
        first = Complex(2, 6)
        second = Complex(2, 5)
        self.assertEqual(Addition(first, second), (4+11j))
   
    
    def test_subtraction(self):
        first = Complex(2, 6)
        second = Complex(2, 5)
        self.assertEqual(Subtraction(first, second), (1j))
        
        
    def test_multiply(self):
        first = Complex(2, 6)
        second = Complex(2, 5)
        self.assertEqual(Multiply(first, second), (-26+22j))
    
    
    def test_division(self):
        first = Complex(2, 6)
        second = Complex(2, 5)
        self.assertEqual(Division(first, second), (1.1724137931034482+0.06896551724137938j))
    

if __name__ == "__main__":
  unittest.main()
```
