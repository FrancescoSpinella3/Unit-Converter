# Unit Converter

FAHRENHEIT = 1
CELSIUS = 2
CENTIMERTERS = 3
INCHES = 4
KILOMETER = 5
MILE = 6


def menu():
    print(">>> Unit Converter")
    print()
    print("Select:")
    print("1. to convert Celsius to Fahrenheit")
    print("2. to convert Fahrenheit to Celsius")
    print("3. to convert Centimeters to Inches")
    print("4. to convert Inches to Centimeters")
    print("5. to convert Miles to Kilometer")
    print("6. to convert Kilometer to Miles")
    print()


def convertion(num):
    choise = int(input("Choise: "))
    while choise < 1 or choise > 6:
        print("Error!!! Insert a valid number")
        choise = int(input("Choise: "))

    if choise == 1:
        degrees_fahrenheit = int(num * 1.8 + 32)
        print(number_to_convert, "°C to Fahrenheit is: ", degrees_fahrenheit, "°F")
    
    elif choise == 2:
        degrees_celsius = int((num - 32) / 1.8)
        print(number_to_convert, "°F to Celsius is: ", degrees_celsius, "°C" )
    
    elif choise == 3:
        centimeter_to_inches = number_to_convert / 2.54
        print(number_to_convert, "cm to inches is: ", centimeter_to_inches, "inches")

    elif choise == 4:
        inches_to_centimeter = number_to_convert * 2.54
        print(number_to_convert, "inches to centimeters is: ", inches_to_centimeter, "cm")
    
    elif choise == 5:
        miles_to_kilometers = number_to_convert * 1.609344
        print(number_to_convert, "miles to km is: ", miles_to_kilometers, "km")

    elif choise == 6:
        kilometers_to_miles = number_to_convert / 1.609344
        print(number_to_convert, "km to Miles is: ", kilometers_to_miles, "miles")


menu()
number_to_convert = int(input("Number to convert: "))
convertion(number_to_convert)

