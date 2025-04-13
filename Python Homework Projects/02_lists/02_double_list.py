def main():
    # Original list of numbers
    numbers = [1, 2, 3, 4]

    # Create a new empty list to store doubled numbers
    doubled_numbers = []

    # Loop through each number in the original list
    for number in numbers:
        double = number * 2          # Double the number
        doubled_numbers.append(double)  # Add it to the new list

    # Print the new list with doubled values
    print(doubled_numbers)


# Required to run the main function
if __name__ == '__main__':
    main()
