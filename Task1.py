def task1():
    # Take input from user for the target position
    n = int(input("Enter the Position: "))

    # s will store the concatenated number string (like "1234567...")
    s = ""

    # i represents the current number that we will append to the string
    i = 1

    # Keep building the string until its length becomes at least n
    while len(s) < n:
        s += str(i)   # Convert i to string and add it to s
        i += 1        # Move to the next number

    # Return the final generated string
    return s

# Call the function and print the final result
print(task1())
