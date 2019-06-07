class Fraction:
    def __init__(self, numerator, denominator):
        """Instantiates the numerator and denomintor
        This allows any Fraction object to be represented by numerator/denominator and insures only valid inputs"""
        """
        self.numerator = numerator
        self.denominator = denominator
        if denominator == 0:
            raise ZeroDivisionError
        """
        try:
            numerator = float(numerator)
            denominator = float(denominator)
            if denominator == 0:
                self.numerator = None
                print ("Denominator can't equal 0!")
                raise ValueError
            else:
                self.numerator = numerator
                self.denominator = denominator        
        except ValueError:
            self.numerator = None       #this is the only necesary check to insure object is invalid
            print("Enter Valid Numerator and Denominator")
            
            
    def __str__(self):
        """Magic function to print the Fraction object in the form 
           numerator/denominator
           rather than printing the object location"""
        if self.numerator is not None:
            return str(self.numerator) + "/" + str(self.denominator)
        else:
            return "Undefined Fraction Object"


    def plus(self, other):
        """Adds the two fractions with the GCF in the denominator"""
        answer_numerator = self.numerator*other.denominator + other.numerator*self.denominator
        answer_denominator = self.denominator*other.denominator
        return Fraction(answer_numerator, answer_denominator)
    
    def minus(self,other):    
        """Subracts the two fractions with the GCF in the denominator"""
        answer_numerator = self.numerator*other.denominator - other.numerator*self.denominator
        answer_denominator = self.denominator*other.denominator
        return Fraction(answer_numerator, answer_denominator)

    def times(self,other):
        """Multiply the two fractions with the GCF in the denominator"""
        answer_numerator = self.numerator*other.numerator
        answer_denominator = self.denominator*other.denominator
        return Fraction(answer_numerator, answer_denominator)

    def divide(self,other):
        """Return a fraction with the quotient of self and other where other is another fraction, returns undefined fraction object if the answer is infinity"""
        answer_numerator = self.numerator*other.denominator
        answer_denominator = self.denominator*other.numerator
        return Fraction(answer_numerator, answer_denominator)

    def equals(self,other):
        """Checks to see if the fractions are equal, returns true or false"""
        if (self.numerator*other.denominator) == (self.denominator*other.numerator):
            value = True
        else:
            value = False
        return value

def test_suite():
    """This checks to see if the program is working properly, this is a test case. We also hand calulated expected values
    for all of the following functions and display them next to program calculated values."""
    test_fraction1 = Fraction(1,2)
    test_fraction2 = Fraction(3,4)
    print ("Expected outputs were hand calculated")
    print ("Fraction 1: "+ str(test_fraction1))
    print ("Fraction 2: "+ str(test_fraction2))
    print (str(test_fraction1) + " + " + str(test_fraction2) + " = " + str(test_fraction1.plus(test_fraction2)) + "\tExpected: 10.0/8.0")
    print (str(test_fraction1) + " - " + str(test_fraction2) + " = " + str(test_fraction1.minus(test_fraction2)) + "\tExpected: -2.0/8.0")
    print (str(test_fraction1) + " * " + str(test_fraction2) + " = " + str(test_fraction1.times(test_fraction2)) + "\tExpected: 3.0/8.0")
    print (str(test_fraction1) + " / " + str(test_fraction2) + " = " + str(test_fraction1.divide(test_fraction2)) + "\tExpected: 4.0/6.0")
    print (str(test_fraction1) + " = " + str(test_fraction2) + " : " + str(test_fraction1.equals(test_fraction2)) + "\tExpected: False")

def calculation(num1,den1,num2,den2,operator):
    """Identifies and performs the proper mathmatical calculation, checking for valid inputs before doing so"""
    f1 = Fraction(num1,den1)
    f2 = Fraction(num2,den2)
    if f1.numerator is not None and f2.numerator is not None:
        if operator == "+":
            print(str(f1) + " + " + str(f2) + " = " + str(f1.plus(f2)))
        elif operator == "-":
            print(str(f1) + " - " + str(f2) + " = " + str(f1.minus(f2)))
        elif operator == "*":
            print(str(f1) + " * " + str(f2) + " = " + str(f1.times(f2)))
        elif operator == "/":
            print(str(f1) + " / " + str(f2) + " = " + str(f1.divide(f2)))
        elif operator == "=":
            print(str(f1) + " = " + str(f2) + " : " + str(f1.equals(f2)))
        else:
            print("Please Enter a Valid Operator")
    

def main():
    """Provides a test case and allows the user to then use the calculator until they choose to stop"""
    print("Welcome to the Fraction Calcultor")
    print("This is our test case to showcase the functions available")
    test_suite()
    print("Now its your turn to experiment with our fraction calculator, please input integer values for the fraction functions")
    while True:
        num1 = input("Fraction 1 numerator: ")
        den1 = input("Fraction 1 denominator: ")
        operator = input("Operation (+,-,*,/,=): ")
        num2 = input("Fraction 2 numerator: ")
        den2 = input("Fraction 2 denominator: ")
        calculation(num1,den1,num2,den2,operator)
        keep = input("Type Stop to end, otherwise continue with calculator: ")
        if keep.lower() == "stop":
            break

if __name__ == '__main__':
    main()