"""
Program: feet_to_inches
------------------------
"""

# Conversion factor: 12 inches in a foot
INCHES_IN_FOOT = 12

def main():
    # Ask user for the number of feet
    feet = float(input("Enter number of feet: "))
    
    # Convert feet to inches
    inches = feet * INCHES_IN_FOOT
    
    # Display the result
    print(f"That is {inches} inches!")

# Required to run the main function
if __name__ == '__main__':
    main()
