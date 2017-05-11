#Elisandra Silva - 10347211

import unittest

from car import *

# testing the car functionality:

class TestCar(unittest.TestCase):
    
    def setUp(self):
        self.car = Car()
        self.petrol_car = PetrolCar()  
        self.diesel_car = DieselCar()
        self.electric_car = ElectricCar() 
        self.hybrid_car = HybridCar()  
        self.angier_car_rental = AngierCarRental()
    
    def test_car_colour(self):
        self.assertEqual('', self.car.getColour())
        self.car.paint('red')
        self.assertEqual('red', self.car.getColour())

    def test_car_make(self):
        self.assertEqual('', self.car.getMake())
        self.car.setMake('Ferrari')
        self.assertEqual('Ferrari', self.car.getMake())
        
    def test_car_model(self):
        self.assertEqual('', self.car.getModel())
        self.car.setModel('488 Spider')
        self.assertEqual('488 Spider', self.car.getModel())
    
    def test_car_mileage(self):
        self.assertEqual(0, self.car.getMileage())
        self.car.move(15)
        self.assertEqual(15, self.car.getMileage())
        
    def test_numberCylindersPetrol(self):
        self.assertEqual(1, self.petrol_car.getNumberCylinders())
        self.petrol_car.setNumberCylinders(2)
        self.assertEqual(2, self.petrol_car.getNumberCylinders())
        
    def test_numberCylindersDiesel(self):
        self.assertEqual(1, self.diesel_car.getNumberCylinders())
        self.diesel_car.setNumberCylinders(4)
        self.assertEqual(4, self.diesel_car.getNumberCylinders())

        
    def test_numberFuelCellsElectric(self):
        self.assertEqual(1, self.electric_car.getNumberFuelCells())
        self.electric_car.setNumberFuelCells(6)
        self.assertEqual(6, self.electric_car.getNumberFuelCells())
        
    def test_numberFuelCellsHybrid(self):
        self.assertEqual(1, self.hybrid_car.getNumberFuelCells())
        self.hybrid_car.setNumberFuelCells(2)
        self.assertEqual(2, self.hybrid_car.getNumberFuelCells())
        
        
    def test_numberCylindersHybrid(self):
        self.assertEqual(1, self.hybrid_car.getNumberCylinders())
        self.hybrid_car.setNumberCylinders(4)
        self.assertEqual(4, self.hybrid_car.getNumberCylinders())

    def test_rent_return(self): 
        self.angier_car_rental.create_current_stock()
        self.assertEqual(20, len(self.angier_car_rental.petrol_cars))
        self.angier_car_rental.rent(self.angier_car_rental.petrol_cars, 5)
        self.assertEqual(15, len(self.angier_car_rental.petrol_cars))

        self.angier_car_rental.return_car(self.angier_car_rental.petrol_cars, 10)
        self.assertEqual(15, len(self.angier_car_rental.petrol_cars))

        self.angier_car_rental.return_car(self.angier_car_rental.petrol_cars, 5)
        self.assertEqual(20, len(self.angier_car_rental.petrol_cars))

       
if __name__ == '__main__':
    unittest.main()


      






