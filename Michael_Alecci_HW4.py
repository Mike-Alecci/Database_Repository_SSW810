import unittest
import random

#here is part one of the homework
def count_vowels(s):
    """This function counts how many vowels are in a string"""
    count=0
    for check in s:
            if check in "aeiouAEIOU":
                count+=1
    return count

#here is part two of the homework
def last_instance_of(target, inputlist):
    """This function returns the last instance of target in inputlist, if it does not occur returns None"""
    instance = None
    for offset, check in enumerate(inputlist):
        if check == target:
            instance = offset
    return instance 

#here is part three which includes the whole fraction class plus the new method simplify
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


    def simplify(self):
        """Simplifies the fractions as much as possible"""
        gcf = 1
        minimum = int(min(abs(self.numerator), abs(self.denominator)))
        for check in range(minimum, 1, -1):
            if self.numerator % check == 0 and self.denominator % check == 0:
                gcf = check
                break
        return Fraction(int(self.numerator/gcf), int(self.denominator/gcf))


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


#here is part four a) of the homework
def infinite_rand_generator(min, max):
    """Returns a random integer between minimum and maximum parameters inclusively everytime its called"""
    while True:
        yield random.randint(min,max)


#here is part four b) of the homework
def find_target(target, min_value, max_value, max_attempts):
    """Attempts to find a target value generated from a random number generator between
       a minimum and maximum value in a certain number of attempts"""
    if target < min_value or target > max_value:
        raise ValueError("Please provide a target within the minimum and maximum constraints")
    attempt = "Not found"
    g = infinite_rand_generator(min_value, max_value)
    for offset in range(max_attempts):
        if target == next(g):
            attempt = offset
            break
    return attempt

class MichaelsHomeworkTest(unittest.TestCase):
    """Tests that my homework works properly"""

    def test_count_vowels(self):
        """Tests the count vowels function works properly"""
        self.assertEqual(count_vowels('hello world'), 3)
        self.assertEqual(count_vowels('hI YOu ThEre'), 5)
        self.assertEqual(count_vowels('hll wrld'), 0)
        self.assertEqual(count_vowels('1234'), 0)
        self.assertEqual(count_vowels(''), 0)

    def test_last_instance_of(self):
        """Tests the last instance of function works properly"""
        self.assertEqual(last_instance_of("h", 'hello world'), 0)
        self.assertEqual(last_instance_of("l", 'hello world'), 9)
        self.assertEqual(last_instance_of("x", 'hello world'), None)
        self.assertEqual(last_instance_of("p", 'apple'), 2)
        self.assertEqual(last_instance_of(33, [12, 33, 44, 55]), 1)
        self.assertEqual(last_instance_of(33, [12, 33, 44, 33]), 3)

    def test_simplify(self):
        """Test that the simplify method works well"""
        f = Fraction(1,2)
        f1 = Fraction(2,4)
        f2 = Fraction(7,21)
        f3 = Fraction(-3,6)
        self.assertTrue(str(f.simplify()) == str(Fraction(1,2)))
        self.assertTrue(str(f1.simplify()) == str(Fraction(1,2)))
        self.assertTrue(str(f3.simplify()) == str(Fraction(-1,2)))
        self.assertTrue(str(f2.simplify()) == str(Fraction(1,3)))

    def test_find_target(self):
        """Tests that the find target method works, meaning so does the infinite random number generator method"""
        self.assertEqual(find_target(3,3,3,1), 0)
        with self.assertRaises(ValueError):
            find_target(5,3,3,1)
        self.assertEqual(find_target(3,3,3,0), "Not found")



if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)