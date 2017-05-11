from calculator import *

error_msg = 'Invalid choice!'
get_menu()

while True:
    print ('Type the corresponding number for calculation or type 0 to quit: ') 
    operator = input()
    try:
        operator = int(operator)
            
        if operator == 0:    
            print ('Quit programme')        
            break
            
        elif operator == 1:
            num1 = getnuminput('Enter the first number: ') 
            num2 = getnuminput('Enter the second number: ')  
            result = add(num1, num2)
            print ('{} + {} = {}' .format(num1, num2, result))
                    
        elif operator == 2:
            num1 = getnuminput('Enter the first number: ') 
            num2 = getnuminput('Enter the second number: ')  
            result = subtract(num1, num2)
            print ('{} - {} = {}' .format(num1, num2, result))
            
        elif operator == 3:
            num1 = getnuminput('Enter the first number: ') 
            num2 = getnuminput('Enter the second number: ')  
            result = multiply(num1, num2)
            print ('{} * {} = {}' .format(num1, num2, result))
            
        elif operator == 4:
            num1 = getnuminput('Enter the first number: ') 
            num2 = getnuminput('Enter the second number: ')  
            result = division(num1, num2)
            print ('{} / {} = {}' .format(num1, num2, result))
            
        elif operator == 5:
            num1 = getnuminput('Enter the first number: ') 
            num2 = getnuminput('Enter the second number: ')  
            result = exponent(num1, num2)
            print ('{} ^ {} = {}' .format(num1, num2, result))
            
        elif operator == 6:
            num1 = getnuminput('Enter number: ') 
            result = factorial_(num1)
            print ('{}! = {}' .format(num1, result))
            
        elif operator == 7:
            num1 = getnuminput('Enter number: ') 
            result = sqrt(num1)
            print ('Square root = {}' .format(result))
            
        elif operator == 8:
            num1 = getnuminput('Enter angle in radians: ') 
            result = sine(num1)
            print ('Sine = ', round(result,4))  
            
        elif operator == 9:
            num1 = getnuminput('Enter angle in radians: ') 
            result = cosine(num1)
            print ('Cosine = ', round(result,4))
            
        elif operator == 10:
            num1 = getnuminput('Enter angle in radians: ') 
            result = tangent(num1)
            print ('Tangent = ', round(result,4))
        else: 
            print (error_msg)
    except:
        print (error_msg)
         



