# Global conversion factors
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9 #no spaces inbetween the numbers


def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global factor."""
    # Note: We don't need 'global' keyword because we're only reading the value
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global factor."""
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    """Handle user interaction and perform conversions."""
    try:
        # Get user input
        temperature = float(input("Enter the temperature to convert: "))  # Raises ValueError if not numeric
        
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
        
        # Perform conversion based on unit
        if unit == 'F':
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted}°C")
        elif unit == 'C':
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted}°F")
        else:
            print("Invalid unit. Please enter either 'C' or 'F'.")
    
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()

