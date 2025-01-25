# Define the height of the pyramid
rows = 5

# Outer loop to control the number of rows
current_row = 1
while current_row <= rows:
    # Inner loop for spaces
    spaces = rows - current_row
    while spaces > 0:
        print(" ", end="")  # Print spaces without a newline
        spaces -= 1
    
    # Inner loop for asterisks
    asterisks = 2 * current_row - 1
    while asterisks > 0:
        print("*", end="")  # Print asterisks without a newline
        asterisks -= 1
    
    # Move to the next line after printing spaces and asterisks for the current row
    print()
    current_row += 1
