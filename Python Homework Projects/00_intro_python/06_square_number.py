def main():
    # Ask the user for a number
    num = float(input("Type a number to see its square: "))
    
    # Calculate the square
    square = num * num
    
    # Display the result
    print(str(num) + " squared is " + str(square))

# Required to run the main function
if __name__ == '__main__':
    main()
