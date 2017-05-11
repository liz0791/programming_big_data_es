#calculator with 10 functions:

#Handling input:    
def getnuminput(str): 
    while True: 
        str_input = input(str) 
        try: 
            fl_value= float(str_input) 
            break 
        except: print ('Input must be numeric!') 
    return fl_value 

    
#calculation functions
def add(num1, num2): 
    return num1 + num2 
    
def subtract(num1, num2): 
    return num1 - num2 
   
def multiply(num1, num2): 
    return num1 * num2 
    
def division(num1, num2): 
    if num2 != 0: 
        return num1 / num2 
    else: 
        return "You can't divide by zero"
       
def exponent(num1, num2):
    return num1 ** num2
    

def factorial_(num1):
   from math import factorial 
   if num1 == int(num1):
       return factorial(num1)
   else:
       return "Factorial only accepts integral values"
   
def sqrt(num1):
    from math import sqrt
    if num1 >= 0:
       return sqrt(num1)
    else: 
       return "The square root of a negative is undefined over the Reals" 
    

def sine(num1):
    from math import sin
    return sin(num1)

def cosine(num1):
    from math import cos
    return cos(num1)

def tangent(num1):  
    from math import tan
    return tan(num1)
    
    
def get_menu():    
    print ('\n*****************************')
    print ('****SCIENTIFIC CALCULATOR****')
    print ('*****************************')
    print ('\n1: ADDITION')
    print ('2: SUBTRACTION')
    print ('3: MULTIPLICATION')
    print ('4: DIVISION')
    print ('5: EXPONENT')
    print ('6: FACTORIAL')
    print ('7: SQUARE ROOT')
    print ('8: SINE')
    print ('9: COSINE')
    print ('10: TANGENT')
    print ('0: QUIT\n')

