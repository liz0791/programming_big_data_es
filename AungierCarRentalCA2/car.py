#Elisandra Silva - 10347211

#Class for car (Superclass)
class Car(object):

#car atributtes:
    
    def __init__(self):
        self.__colour = ''
        self.__make = ''
        self.__model = ''
        self.__mileage = 0
        self.engineSize = ''

    def getColour(self):
        return self.__colour

    def getMake(self):
        return self.__make
        
    def getModel(self):
        return self.__model

    def getMileage(self):
        return self.__mileage

    def setColour(self, colour):
        self.__colour = colour

    def setMake(self, make):
        self.__make = make
        
    def setModel(self, model):
        self.__model = model

    def setMileage(self, mileage):
        self.__mileage = mileage

    def paint(self, colour):
        self.__colour = colour
        return self.__colour

    def move(self, distance):
        self.__mileage = self.__mileage + distance
        return self.__mileage

#Subclasses - giving each car specific characteristics  
class ElectricCar(Car):
    
    def __init__(self):
        Car.__init__(self)
        self.__numberFuelCells = 1

    def getNumberFuelCells(self):
        return self.__numberFuelCells

    def setNumberFuelCells(self, value):
        self.__numberFuelCells = value

class PetrolCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__numberCylinders = 1

    def getNumberCylinders(self):
        return self.__numberCylinders

    def setNumberCylinders(self, value):
        self.__numberCylinders = value
        
        
class DieselCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__numberCylinders = 1

    def getNumberCylinders(self):
        return self.__numberCylinders

    def setNumberCylinders(self, value):
        self.__numberCylinders = value

        
class HybridCar(Car):
    
    def __init__(self):
        Car.__init__(self)
        self.__numberFuelCells = 1
        self.__numberCylinders = 1

    def getNumberFuelCells(self):
        return self.__numberFuelCells

    def setNumberFuelCells(self, value):
        self.__numberFuelCells = value

    def getNumberCylinders(self):
        return self.__numberCylinders

    def setNumberCylinders(self, value):
        self.__numberCylinders = value
        
        
#subclass to create stock, rent and return cars
class AngierCarRental(Car):

    def __init__(self):
        self.petrol_cars = []
        self.diesel_cars = []
        self.electric_cars = []  
        self.hybrid_cars = []
        

    def create_current_stock(self):
        for i in range(20):
            self.petrol_cars.append(PetrolCar())
        for i in range (8):
            self.diesel_cars.append(DieselCar())
        for i in range(4):
            self.electric_cars.append(ElectricCar())
        for i in range (8):
            self.hybrid_cars.append(HybridCar())
        
    def stock_count(self):
        print ('petrol cars in stock: ' + str(len(self.petrol_cars)))
        print ('diesel cars in stock: ' + str(len(self.diesel_cars)))
        print ('electric cars in stock: ' + str(len(self.electric_cars)))
        print ('hybrid cars in stock: ' + str(len(self.hybrid_cars)))
        

    def rent(self, car_list, amount):
        if len(car_list) < amount:
            print ("Sorry nothing to rent, please try again")
            return
        total = 0
        while total < amount:
           car_list.pop()
           total = total + 1
           
           
    def return_car(self, car_list, amount):
        if len(self.petrol_cars) + amount > 20 and len(self.diesel_cars) + amount > 8 and len(self.electric_cars) + amount > 4 and len(self.hybrid_cars) +amount > 8:
            print ('It seems that item(s) have been returned already!')
            return
        total = 0
        while total < amount:
            car_list.append(amount)
            total = total + 1
            
    def get_option(self, str):
        error_msg = 'Invalid choice!\n'
        while True: 
            str_option = raw_input(str) 
            try: 
                int_option= int(str_option) 
                break 
            except: print (error_msg) 
        return int_option 
    
   
    def process_rental(self): #handling input and applying rent/return functions
        
        error_msg = 'Invalid choice!\n'
        action = self.get_option('Type "1" to rent  or "2" to return: \n')
        if action == 1:
            amount = self.get_option('How many cars would you like to rent? \n')
            action = raw_input('Type "p" for petrol, "d" for diesel, "e" for eletric or "h" for hybrid: \n')
            if action == 'p':
                self.rent(self.petrol_cars, amount)
            elif action == 'd':
                self.rent(self.diesel_cars, amount)    
            elif action == 'e':
                self.rent(self.electric_cars, amount)
            elif action == 'h':
                self.rent(self.hybrid_cars, amount)
            else:
                print (error_msg)
                
        elif action == 2:
            amount = self.get_option('How many cars are you returning? \n')
            action = raw_input('Type "p" for petrol, "d" for diesel, "e" for eletric or "h" for hybrid: \n')
            if action == 'p':
                self.return_car(self.petrol_cars, amount)
            elif action == 'd':
                self.return_car(self.diesel_cars, amount)    
            elif action == 'e':
                self.return_car(self.electric_cars, amount)
            elif action == 'h':
                self.return_car(self.hybrid_cars, amount)
            else:
                print (error_msg) 
                
        else:
            print (error_msg)
			
        self.stock_count()



