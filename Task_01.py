def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def convert_temperature():
    try:
        value = float(input("Enter the temperature value: "))
        unit = input("Enter the unit (C for Celsius, F for Fahrenheit, K for Kelvin): ").strip().upper()

        if unit == 'C':
            print(f"{value}°C = {celsius_to_fahrenheit(value):.2f}°F")
            print(f"{value}°C = {celsius_to_kelvin(value):.2f}K")
        elif unit == 'F':
            print(f"{value}°F = {fahrenheit_to_celsius(value):.2f}°C")
            print(f"{value}°F = {fahrenheit_to_kelvin(value):.2f}K")
        elif unit == 'K':
            print(f"{value}K = {kelvin_to_celsius(value):.2f}°C")
            print(f"{value}K = {kelvin_to_fahrenheit(value):.2f}°F")
        else:
            print("Invalid unit. Please enter C, F, or K.")
    except ValueError:
        print("Invalid temperature value. Please enter a numeric value.")

# Run the conversion
convert_temperature()
