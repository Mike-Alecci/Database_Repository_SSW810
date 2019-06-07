'''The function of this program is to allow the user to convert fahrenheit temperatures to celcius, 
this is accomplished using two different methods. One method is a simple calculator function for arbitrary 
temperatures. The other method checks to see if the input matches the number 6 train stops which have integer 
celcius conversions and returns them. This program provides prompted user interaction.'''

def fahrenheit2celsius(f):
    '''Converts an arbitrary temperature in fahrenheit to celcius
    using the standard formula T(°C) = (T(°F) - 32) × 5/9'''
    return (f-32)*(5/9)

def f2c_6train(f):
    '''Determines if the input fahrenheit value matches any of the Number
    6 train stops then returns the corresponding celcius conversion, includes a 
    guard value of -9999 for values that do not correspond'''
    if f == 86:
        return 30
    elif f == 77:
        return 25
    elif f == 68:
        return 20
    elif f == 59:
        return 15
    elif f == 50:
        return 10
    elif f == 41:
        return 5
    elif f == 32:
        return 0
    elif f == 23:
        return -5
    elif f == 14:
        return -10
    return -9999

def f2c(f):
    '''Choose if the given input matches one of the Number 6 train stops,
    if True then the f2c_6train method runs, else the method runs fahrenheit2celsius(f)'''
    trainCheck = f2c_6train(f)
    if -9999 == trainCheck:
        return fahrenheit2celsius(f)
    return trainCheck

def is_float(check):
    '''Checks if the input value is a valid input of int or float type, returns false if the type is inconsistent with desired type'''
    try: 
        float(check)
        return True
    except ValueError:
        return False

def main():
    '''This first proves the calculations are correct. Then allows the user to convert values as prompted, only allows
     valid numbers (ints, floats not strings) runs continuously through a while loop that can be broken by typing stop'''
    print ('Here are some numbers just to prove this works with valid inputs, try your own below!')
    print ('Input:' , 54 , 'Computed Value:' , f2c(54) , 'Expected Value:' , 12.2222222223)
    print ('Input:' , 14 , 'Computed Value:' , f2c(14) , 'Expected Value:' , -10)
    print ('Input:' , 32 , 'Computed Value:' , f2c(32) , 'Expected Value:' , 0)
    print ('Input:' , -40 , 'Computed Value:' , f2c(-40) , 'Expected Value:' , -40)
    while True:
        value = input('Provide your value to convert from Fahrenheit to Celcius, enter stop to finish, Value: ')
        if is_float(value):
            value = float(value)
            print ('Input:' , value , 'Computed Value:' , f2c(value))
        elif value == 'stop':
            break
        else:
            print ('Please provide a valid input')

if __name__ == '__main__':
    main()
