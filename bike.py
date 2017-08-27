class Bike(object):
    def __init__(self):
        self.price = 200
        self.maxSpeed = '25mph'
        self.miles = 0
    def displayInfo(self):
        print self.price
        print self.maxSpeed
        print self.miles
    def ride(self):
        print 'Riding'
        self.miles += 10
        return self
    def reverse(self):
        print 'Reversing'
        self.miles -= 5
        if self.miles < 0:
            self.miles = 0 #by setting a condition and setting a minimum miles per hour
        return self

bikeTesla = Bike()
bikeTesla.ride().ride().ride().reverse().displayInfo()

bikeBenz = Bike()
bikeBenz.ride().ride().reverse().reverse().displayInfo()

bikeWurry = Bike()
bikeWurry.reverse().reverse().reverse().displayInfo()
