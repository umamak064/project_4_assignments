# Program: add2numbers
# --------------------
# This program asks the user for two integers and prints their sum.

def main():
    print("This program adds two numbers.")

    # Ask the user for the first number
    num1 = input("Enter first number: ")
    num1 = int(num1)  # Convert the input to an integer

    # Ask the user for the second number
    num2 = input("Enter second number: ")
    num2 = int(num2)  # Convert the input to an integer

    # Add the numbers
    total = num1 + num2

    # Display the result
    print("The total is " + str(total) + ".")

# Make sure the main function runs when the script is executed
if __name__ == '__main__':
    main()
