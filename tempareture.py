"""Write a convertToFahrenheit() function with a degreesCelsius parameter. This
function returns the number of this temperature in degrees Fahrenheit.
 Then write a function named
convertToCelsius() with a degreesFahrenheit parameter and returns a number of this
temperature in degrees Celsius.
Use these two formulas for converting between Celsius and Fahrenheit:
 Fahrenheit = Celsius × (9 / 5) + 32
 Celsius = (Fahrenheit - 32) × (5 / 9)
These Python assert statements stop the program if their condition is False. Copy them to
the bottom of your solution program. Your solution is correct if the following assert statements’
conditions are all True:
assert convertToCelsius(0) == -17.77777777777778
assert convertToCelsius(180) == 82.22222222222223
assert convertToFahrenheit(0) == 32
assert convertToFahrenheit(100) == 212
assert convertToCelsius(convertToFahrenheit(15)) == 15
# Rounding errors cause a slight discrepancy:
assert convertToCelsius(convertToFahrenheit(42)) == 42.00000000000001
Try to write a solution based on the information in this description. If you still have trouble
solving this exercise, read the Solution Design and Special Cases and Gotchas sections for
additional hints.
"""
def convertToFahrenheit(degreesCelsius):
    # Calculate and return the degrees Fahrenheit:
    return degreesCelsius * (9 / 5) + 32


def convertToCelsius(degreesFahrenheit):
    # Calculate and return the degrees Celsius:
    return (degreesFahrenheit - 32) * (5 / 9)

assert convertToCelsius(0) == -17.77777777777778
assert convertToCelsius(180) == 82.22222222222223
assert convertToFahrenheit(0) == 32
assert convertToFahrenheit(100) == 212
assert convertToCelsius(convertToFahrenheit(15)) == 15

# Rounding errors cause a slight discrepancy:
assert convertToCelsius(convertToFahrenheit(42)) == 42.00000000000001


