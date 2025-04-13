def main():
    # Ask the user for each side length and convert it to float
    side1 = float(input("What is the length of side 1? "))
    side2 = float(input("What is the length of side 2? "))
    side3 = float(input("What is the length of side 3? "))

    # Calculate the perimeter
    perimeter = side1 + side2 + side3

    # Display the result
    print("The perimeter of the triangle is " + str(perimeter))

# Required to run the main function
if __name__ == '__main__':
    main()
