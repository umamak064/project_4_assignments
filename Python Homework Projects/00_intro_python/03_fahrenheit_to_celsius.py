def main():
    # Ask the user to enter temperature in Fahrenheit
    temp_f = input("Enter temperature in Fahrenheit: ")
    
    # Convert the input to a float for decimal support
    temp_f = float(temp_f)
    
    # Convert to Celsius using the given formula
    temp_c = (temp_f - 32) * 5.0 / 9.0

    # Display the result with both temperatures
    print("Temperature:", str(temp_f) + "F =", str(temp_c) + "C")

# This line ensures main() runs when the script is executed
if __name__ == '__main__':
    main()
