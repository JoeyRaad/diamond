# Function to print the diamond star pattern
def print_diamond(rows):

    # Upper part of the diamond
    for i in range(rows):

        # Print leading spaces
        for j in range(rows - i - 1):
            print(" ", end="")
        # Print stars
        for k in range(2 * i + 1):
            print("*", end="")
        print()  

    # Lower part of the diamond
    for i in range(rows - 1):

        # Print leading spaces
        for j in range(i + 1):
            print(" ", end="")
        # Print stars
        for k in range(2 * (rows - i - 2) + 1):
            print("*", end="")
      print()  

# Main program
def main()
    rows = int(input("Enter the number of rows for the diamond pattern: "))
    
    print_diamond(rows)

# Run main program
if __name__ == "__main__":
    main()

