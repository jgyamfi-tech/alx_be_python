# pattern_drawing.py

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Validate that the size is a positive integer
if size <= 0:
    print("Please enter a positive integer.")
else:
    # Initialize the row counter
    row = 0

    # Use a while loop to iterate through rows
    while row < size:
        # Use a for loop to print asterisks in each row
        for _ in range(size):
            print("*", end="")  # Print asterisk without moving to the next line
        print()  # Print a newline character to move to the next row
        row += 1
