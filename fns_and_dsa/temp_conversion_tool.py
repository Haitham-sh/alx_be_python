FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
  return fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
  return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR


temperature = float(input("Enter the temperature to convert: "))
Celsius_or_Fahrenheit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if Celsius_or_Fahrenheit == "c":
  print(f"{temperature}°C is {convert_to_fahrenheit(temperature)}°F")
elif Celsius_or_Fahrenheit == "f":
  print(f"{temperature}°F is {convert_to_celsius(temperature)}°C")
else:
  print("Invalid temperature. Please enter a numeric value.")
