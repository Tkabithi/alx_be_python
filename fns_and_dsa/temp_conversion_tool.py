# temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FREEZING_POINT_F = 32  # Constant used in both conversions

def convert_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius using the global factor."""
    return (fahrenheit - FREEZING_POINT_F) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit using the global factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FREEZING_POINT_F

def main():
    try:
        temp_input = input("Enter the temperature to convert: ").strip()
        temp_value = float(temp_input)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == 'F':
        celsius = convert_to_celsius(temp_value)
        print(f"{temp_value}°F is {celsius}°C")
    elif unit == 'C':
        fahrenheit = convert_to_fahrenheit(temp_value)
        print(f"{temp_value}°C is {fahrenheit}°F")
    else:
        raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()

