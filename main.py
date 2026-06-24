# main.py

import sys

try:
    from temperature_converter import TemperatureConverter
    from input_taker import get_input, get_temperature_input
except ModuleNotFoundError:
    print("Essential module not found to start program")
    sys.exit(1)

def main():
    converter = TemperatureConverter()
    
    options = ["1", "2", "3", "4", "5", "6", "q"]

    while True:
        print("\n" + "=" * 40)
        print("TEMPERATURE CONVERTER SYSTEM")
        print("=" * 40)
        print("[1] Celsius To Kelvin")
        print("[2] Kelvin To Celsius")
        print("[3] Celsius To Fahrenheit")
        print("[4] Fahrenheit To Celsius")
        print("[5] Fahrenheit To Kelvin")
        print("[6] Kelvin To Fahrenheit")
        print("[q] Exit")
        print("=" * 40)

        choice = get_input("Select an option", options)

        if choice == "q":
            print("\nGoodbye! See you again")
            break

        temp = get_temperature_input("Enter the temperature value")

        try:
            if choice == "1":
                res = converter.celsius_to_kelvin(temp)
                print(f"Result: {temp}°C = {res}K")
            elif choice == "2":
                res = converter.kelvin_to_celsius(temp)
                print(f"Result: {temp}K = {res}°C")
            elif choice == "3":
                res = converter.celsius_to_fahrenheit(temp)
                print(f"Result: {temp}°C = {res}°F")
            elif choice == "4":
                res = converter.fahrenheit_to_celsius(temp)
                print(f"Result: {temp}°F = {res}°C")
            elif choice == "5":
                res = converter.fahrenheit_to_kelvin(temp)
                print(f"Result: {temp}°F = {res}K")
            elif choice == "6":
                res = converter.kelvin_to_fahrenheit(temp)
                print(f"Result: {temp}K = {res}°F")

        except ValueError as e:
            print(f"\nError: {e}")


if __name__ == "__main__":
    main()