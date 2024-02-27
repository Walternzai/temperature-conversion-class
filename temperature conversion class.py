class Temperature:
    def convert_fahrenheit(self, celsius):
        """
        Converts Celsius to Fahrenheit and prints the result.
        """
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is approximately {fahrenheit:.2f}°F.")

    def convert_celsius(self, fahrenheit):
        """
        Converts Fahrenheit to Celsius and prints the result.
        """
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is approximately {celsius:.2f}°C.")

# Example usage:
temp = Temperature()
temp.convert_fahrenheit(25)  # Convert 25°C to Fahrenheit
temp.convert_celsius(77)     # Convert 77°F to Celsius
