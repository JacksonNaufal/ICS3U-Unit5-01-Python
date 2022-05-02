#!/usr/bin/env python3

# Created by: Jackson Naufal
# Created on: March 2022
# This is fahrenheit to celsius converter


def temperature_function():

    temperature_string = input("Enter Your Temperature In °C: ")

    try:
        temperature = int(temperature_string)
        fahrenheit_conversion = round((temperature * 9 / 5) + 32, 2)

        # output
        print("{0}°C is equal to {1}°F".format(temperature, fahrenheit_conversion))
    except Exception:
        print("\nThat was not an integer")


def main():

    # call function
    temperature_function()
    print("\nDone.")


if __name__ == "__main__":
    main()
