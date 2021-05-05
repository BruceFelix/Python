"""
A simple program to help convert from Metric to SI units anything you all
do at CSA which uses the same system as any other commonwealth country.
"""
def options():
    print("""
    Options:
    [C] Convert from Celcius to Fahrenheit
    [F] Convert from Fahrenheit to Celcius
    [NM] Convert from Nautical Miles to Kilometers
    [KMNM] Convert from Kilometers to Nautical Miles
    [M] Convert from Miles to Kilometers
    [KM] Convert from Kilometers to Miles
    [CM] Convert centimeters to meters
    [MC] Convert meters to centimeters
    [Y] Convert yards to meters
    [MY] Convert meters to yards
    [IN] Convert from Inches to Centimeters
    [CM] Convert from Centimeters to Inches
    [Q] To Quit
    """) 
print("====================================================")
print("Welcome to my universal Metric to SI units converter")
print("====================================================")
options()
option = True
while option: 
    option = input("Enter your option \n").upper()
    if option == "C":
        #converting from celcius to Fahrenheit
        celcius = float(input("Enter the temperature\n"))
        fahrenheit =(celcius * 9/5) + 32
        print("Fahrenheit: " + str(fahrenheit))
        options()
    elif option == "F":
        #converting from Fahrenheit to Celcius
        fahrenheit = float(input("Enter the temperature\n"))
        celcius = 5/9 * (fahrenheit -32)
        print("Celcius: " + str(celcius))
        options()
    elif option == "NM":
        #Converting from Nautical Miles to Kilometers
        nautical = float(input("Enter the nautical miles to convert\n"))
        kilometer = nautical * 1.852
        print("Kilometers from Nauticals: " + str(kilometer))
        options()
    elif option == "KMNM":
        # Converting from Kilometers to Nautical miles
        kilometer = float(input("Enter the kilometers to convert\n"))
        nautical = kilometer * 0.53996
        print("Nautical miles from Kilometers " + str(nautical))
        options()
    elif option == "M":
        #converting from Miles to Kilometers
        miles = float(input("Enter the miles to convert\n"))
        kilometer = miles * 1.609
        print("Kilometers: " + str(kilometer))
        options()
    elif option == "KM":
        #converting from Kilometer to Miles
        kilometer = float(input("Enter the Kilometers to convert\n"))
        miles = kilometer / 1.609
        print("Miles: " + str(miles))
        options()
    elif option =="CM":
        #Converting centimeters to Meters
        centimeters = float(input("Enter the centimeters to convert\n"))
        meters = centimeters / 100
        print("Meters: "+ str(meters))
        options()
    elif option == "MC":
        #Converting Meters to centimeters
        meters = float(input("Enter the meters to convert\n"))
        centimeters = meters * 100
        print("Centimeters: "+ str(centimeters))
        options()
    elif option == "Y":
        #Convert yards to meters
        yards = float(input("Enter the yards to convert\n"))
        meters = yards * 0.9144
        print("Meters: " + str(meters))
        options()
    elif option == "MY":
        #Comverting meters to yards
        meters = float(input("Enter the meters you want to convert\n"))
        yards = meters / 0.9144
        print("Yards: " + str(yards))
        options()
    elif option == "IN":
        #converting from Inches to Centimeters
        inches = float(input("Enter the inches to convert\n"))
        centimeters = inches * 2.54
        print("Centimeters: " + str(centimeters))
        options()
    elif option == "CTOM":
        #converting from centimeters to inches
        centimeters = float(input("Enter the centimetrs to convert\n"))
        inches = centimeters / 2.54
        print("Inches: " + str(inches))
        options()
    elif option == "Q":
        break
    else:
        print("Invalid input try again")

# print("====================================================")
# print("Welcome to my universal Metric to SI units converter")
# print("====================================================")
# options()
# option = True
# while option == True:
#     conversion()    
