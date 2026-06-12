def to_fahrenheit(celsius):
    return round(celsius * 9 / 5 + 32, 1)

celsius = float(input("Temperature in Celsius:\n"))

print (f"{celsius}°C is {to_fahrenheit(celsius)}°F")