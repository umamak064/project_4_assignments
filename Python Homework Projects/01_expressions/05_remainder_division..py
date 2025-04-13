def main():
    # Get the numbers we want to divide
    dividend = int(input("Please enter an integer to be divided: "))
    divisor = int(input("Please enter an integer to divide by: "))

    # Perform integer division and get the remainder
    quotient = dividend // divisor  # Division result (integer part)
    remainder = dividend % divisor  # Remainder of the division

    # Output the results
    print(f"The result of this division is {quotient} with a remainder of {remainder}")

# Call the main function to run the program
if __name__ == '__main__':
    main()
