def task2():
    # Take the position from the user
    pos = int(input("Enter position: "))

    # s stores the growing sequence like "12345678910..."
    s = ""
    
    # n is the current number being added to the sequence
    n = 1

    # Step 1: Build the sequence until its length reaches or crosses 'pos'
    while len(s) < pos:
        s += str(n)   # Convert n to string and append to s
        n += 1        # Move to the next number

    # Step 2: Find which number lies at the given position
    length = 0   # Tracks how many characters we have counted so far

    # Loop through all numbers added so far
    for i in range(1, n):
        new_str = str(i)          # Convert number to string
        length += len(new_str)    # Add its length to cumulative count

        # When cumulative length becomes >= pos,
        # that means this number contains the desired position
        if length >= pos:
            print("Number at that position is:", i)
            break


# Call the function
task2()