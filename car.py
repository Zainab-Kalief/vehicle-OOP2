class Car(object):

    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.displayAll()

    def displayAll(self):
        allInfo = 'Price: ' + str(self.price) + '\nSpeed: ' + str(self.speed) + '\nFuel: ' + str(self.fuel) + '\nMileage: ' + str(self.mileage) + '\nTax: ' + str(self.tax)
        return allInfo


tesla = Car(4000,200,5,15)

print tesla.displayAll() #we dont need to pass in anything here cos its called on self
#OR
print Car.displayAll(tesla) #we can call the method but we have to pass in the self as the argument that we want to affect, self is the instance
#and we can pass in as many instances we want here
