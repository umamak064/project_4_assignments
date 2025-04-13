"""
Program: einstein_energy
------------------------
"""

# Speed of light in meters per second
C = 299_792_458

def main():
    # Ask the user to enter mass in kilograms
    mass = float(input("Enter kilos of mass: "))

    # Show the formula being applied
    print("\ne = m * C^2...")
    print("m =", mass, "kg")
    print("C =", C, "m/s")

    # Compute energy in joules
    energy = mass * (C ** 2)

    # Output the result
    print(f"\n{energy} joules of energy!")

# Call the main function
if __name__ == '__main__':
    main()
