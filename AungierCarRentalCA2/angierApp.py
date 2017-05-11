#Elisandra Silva - 10347211

from car import *

#populating 2 instances for Class car and 2 of its subclasses (PetrolCar and ElectricCar)
car1 = Car()
car1.setMake('Opel')
print ('Make ' + car1.getMake())
car1.setModel('Corsa')
print ('Model ' + car1.getModel())
car1.setColour('Black')
print ('Colour ' + car1.getColour())
car1.engineSize = '2.9'
print ('Engine Size ' + car1.engineSize)
car1.setMileage(150)
print ('Mileage ' + str(car1.getMileage()))
print ('Car moved ' + str(car1.move(15)) + 'kms')


car2 = Car()
car2.setMake('Volkswagen')
print ('Make ' + car2.getMake())
car2.setModel('Golf')
print ('Model ' + car2.getModel())
car2.engineSize = '3.9'
print ('Engine Size ' + car2.engineSize)
car2.setColour ('Red')
print ('Colour ' + car2.getColour())
car2.setMileage(100)
print ('Mileage ' + str(car2.getMileage()))
print ('Car moved ' + str(car2.move(35)) + 'kms')


car1 = PetrolCar()
car1.setNumberCylinders(4)
print ('Cylinders ' + str(car1.getNumberCylinders()))

car2 = ElectricCar()
car2.setNumberFuelCells(6)
print ('Cells ' + str(car2.getNumberFuelCells()))


#calling methods of Class Car and it's subclasses PetrolCar, DieselCar, ElectricCar, HybridCar and Car Rental 
print ('*********************************')               
print ('**Welcome to Angier Car Rental!**')
print ('*********************************') 

angier_car_rental = AngierCarRental()
angier_car_rental.create_current_stock()

proceed = 'y'
while proceed == 'y':
    angier_car_rental.process_rental()
    proceed = raw_input('Type "y" to continue or any other key to finish: ')
    proceed = proceed.lower()
