rows = 5

# Outer loop to iterate through each row
for i in range(1, rows + 1):
    # Inner loop to print stars for the current row
    # The number of stars to print is equal to the current row number 'i'
    for j in range(i):
        print("*", end="")
    # Move to the next line after the stars in a row are printed
    print()
