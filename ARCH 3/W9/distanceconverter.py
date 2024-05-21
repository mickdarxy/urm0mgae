#create a class named Converter
class Converter:
    #implement the dunder init with default values
    def __init__(self, length, unit):

    #create the if statements needed to make options for the conversions
    #length defaults to meters
        if unit == "meters":
            self.length = length
            self.unit = unit
        elif unit == "kilometers":
            self.length = length * 1000
            self.unit = unit
        elif unit == "centimeters":
            self.length = length / 100
            self.unit = unit
        elif unit == "millimeters":
            self.length = length / 1000
            self.unit = unit
        elif unit == "feet":
            self.length = length / 3.280839895
            self.unit = unit
        elif unit == "inches":
            self.length = length / 39.37
            self.unit = unit
        elif unit == "yards":
            self.length = length / 1.0936132983
            self.unit = unit
        elif unit == "miles":
            self.length = length * 1609.344
            self.unit = unit
        else:
            raise ValueError("ERROR")

    # create useful function for each unit
    def meters(self):
        return self.length

    def kilometers(self):
        return self.length / 1000

    def centimeters(self):
        return self.length * 100

    def millimeters(self):
        return self.length * 1000

    def feet(self):
        return self.length * 3.280839895

    def inches(self):
        return self.length * 39.37

    def yards(self):
        return self.length * 1.0936132983

    def miles(self):
        return self.length / 1609.344



'''Criteria:
The user will pass a length and a unit when declaring an object from the class—for example, c =
Converter(9,'inches').For each of these units there should be a method that
returns the length converted into those units. For example, using the Converter object created above, 
the user could call c.feet() and should get 0.75 as the result.
Use meters as base unit to convert to and from (this prevents rounding errors)
Units:
inches
feet
yards
miles
kilometers
meters
centimeters
millimeters'''