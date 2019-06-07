import unittest

class Fraction:
    "Allows simple mathmatical calulations to be preformed on fractions"
    def __init__(self, numerator, denominator):
        """Instantiates the numerator and denomintor
        This allows any Fraction object to be represented by numerator/denominator and raises an exception if denominator is 0
        or if inputs are invalid"""
        try:
            numerator =float(numerator)
            denominator= float(denominator)
        except ValueError:
            raise ValueError ("Invalid input")
        self.numerator = numerator
        self.denominator = denominator
        if denominator == 0:
            raise ZeroDivisionError ("Can't divide by zero!")

            
    def __str__(self):
        """Magic function to print the Fraction object in the form 
           numerator/denominator
           rather than printing the object location"""
        return str(self.numerator) + "/" + str(self.denominator)


    def __add__(self, other):
        """Adds the two fractions with the GCF in the denominator"""
        answer_numerator = self.numerator*other.denominator + other.numerator*self.denominator
        answer_denominator = self.denominator*other.denominator
        return Fraction(answer_numerator, answer_denominator)
    

    def __sub__(self,other):    
        """Subracts the two fractions with the GCF in the denominator"""
        answer_numerator = self.numerator*other.denominator - other.numerator*self.denominator
        answer_denominator = self.denominator*other.denominator
        return Fraction(answer_numerator, answer_denominator)


    def __mul__(self,other):
        """Multiply the two fractions with the GCF in the denominator"""
        answer_numerator = self.numerator*other.numerator
        answer_denominator = self.denominator*other.denominator
        return Fraction(answer_numerator, answer_denominator)


    def __truediv__(self,other):
        """Return a fraction with the quotient of self and other where other is another fraction, returns undefined fraction object if the answer is infinity"""
        answer_numerator = self.numerator*other.denominator
        answer_denominator = self.denominator*other.numerator
        return Fraction(answer_numerator, answer_denominator)


    def __eq__(self,other):
        """Checks to see if the fractions are equal, returns true or false"""
        if (self.numerator*other.denominator) == (self.denominator*other.numerator):
            value = True
        else:
            value = False
        return value


    def __ne__(self,other):
        """Checks to see if the fractions are not equal, returns true or false"""
        if (self.numerator*other.denominator) != (self.denominator*other.numerator):
            value = True
        else:
            value = False
        return value


    def __lt__(self,other):
        """Checks to see if the first fraction is less than the other, returns true or false"""
        if (self.numerator*other.denominator) < (self.denominator*other.numerator):
            value = True
        else:
            value = False
        return value


    def __le__(self,other):
        """Checks to see if the first fraction is less than or equal to the other, returns true or false"""
        if (self.numerator*other.denominator) <= (self.denominator*other.numerator):
            value = True
        else:
            value = False
        return value


    def __gt__(self,other):
        """Checks to see if the first fraction is greater than the other, returns true or false"""
        if (self.numerator*other.denominator) > (self.denominator*other.numerator):
            value = True
        else:
            value = False
        return value


    def __ge__(self,other):
        """Checks to see if the first fraction is greater than or equal to the other, returns true or false"""
        if (self.numerator*other.denominator) >= (self.denominator*other.numerator):
            value = True
        else:
            value = False
        return value



class FractionTest(unittest.TestCase):
    """An automated test case to insure the class Fraction works porperly"""
    def test_init(self):
        """Tests the Fraction class init method to properly create numerators and denominators"""
        f= Fraction(5,12)
        self.assertEqual(f.numerator, 5)
        self.assertEqual(f.denominator, 12)
        with self.assertRaises(ValueError):
            f1 = Fraction(" ",3)
        with self.assertRaises(ZeroDivisionError):
            f2 = Fraction(1,0)

    def test_str(self):
        """Tests that __str__() works correctly"""
        f = Fraction(1,2)
        self.assertEqual(str(f), "1.0/2.0")

    def test_add(self):
        """Tests that __add__() works correctly"""
        f = Fraction(1,2)
        f1 = Fraction(3,4)
        f2 = Fraction(2,3)
        self.assertTrue(f+f1 == Fraction(10,8))
        self.assertTrue(f+f == Fraction(4,4))
        self.assertTrue(f+f2 == Fraction (7,6))

    def test_sub(self):
        """Tests that __sub__() works correctly"""
        f = Fraction(1,2)
        f1 = Fraction(3,4)
        f2 = Fraction(2,3)
        self.assertTrue(f1-f1 == Fraction(0,16))
        self.assertTrue(f1-f == Fraction(2,8))
        self.assertTrue(f2-f == Fraction (1,6))

    def test_mul(self):
        """Tests that __mul__() works correctly"""
        f = Fraction(1,2)
        f1 = Fraction(3,4)
        f2 = Fraction(2,3)
        self.assertTrue(f1*f1 == Fraction(9,16))
        self.assertTrue(f1*f == Fraction(3,8))
        self.assertTrue(f2*f == Fraction (2,6))

    def test_truediv(self):
        """Tests that __truediv__() works correctly"""
        f = Fraction(1,2)
        f1 = Fraction(3,4)
        f2 = Fraction(2,3)
        self.assertTrue(f1/f1 == Fraction(12,12))
        self.assertTrue(f1/f == Fraction(6,4))
        self.assertTrue(f2/f == Fraction (4,3))
        with self.assertRaises(ZeroDivisionError):
            f/Fraction(0,3)
      
    def test_eq(self):
        """Tests that __eq__() works correctly"""
        f = Fraction(1,2)
        f1 = Fraction(2,4)
        f2 = Fraction(4,4)
        self.assertTrue(f == f1)
        self.assertTrue(f+f1 == f2)
        self.assertFalse(f == f2)
        self.assertFalse(f == Fraction(2,1))

    def test_ne(self):
        """Tests that __ne__() works correctly"""
        f = Fraction(1,2)
        f1 = Fraction(2,4)
        f2 = Fraction(4,4)
        self.assertFalse(f != f1)
        self.assertFalse(f+f1 != f2)
        self.assertTrue(f != f2)
        self.assertTrue(f != Fraction(2,1))

    def test_lt(self):
        """Tests that __lt__() works correctly"""
        f = Fraction(1,2)
        f1 = Fraction(3,2)
        f2 = Fraction(2,2)
        self.assertTrue(f < f2)
        self.assertTrue(f2 < f1)
        self.assertFalse(f1 < f)

    def test_le(self):
        """Tests that __le__() works correctly"""
        f = Fraction(1,2)
        f1 = Fraction(3,2)
        f2 = Fraction(2,2)
        self.assertTrue(f <= f2)
        self.assertTrue(f2 <= f2)
        self.assertTrue(f+f2 <= f1)
        self.assertFalse(f1 <= f)

    def test_gt(self):
        """Tests that __gt__() works correctly"""
        f = Fraction(1,2)
        f1 = Fraction(3,2)
        f2 = Fraction(2,2)
        self.assertTrue(f2 > f)
        self.assertTrue(f1 > f2)
        self.assertFalse(f > f1)

    def test_ge(self):
        """Tests that __ge__() works correctly"""
        f = Fraction(1,2)
        f1 = Fraction(3,2)
        f2 = Fraction(2,2)
        self.assertTrue(f2 >= f)
        self.assertTrue(f2 >= f2)
        self.assertTrue(f1 >= f+f2)
        self.assertFalse(f >= f1)

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)