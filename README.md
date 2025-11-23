# Task1 – Number Sequence Generator

This project contains a simple Python program that generates a continuous sequence of natural numbers (like "12345678910...") until the total length reaches the user-given position.


---

#How It Works

1. The user enters a number n


2. The program keeps appending numbers starting from 1 ("1", "2", "3", …)


3. It stops only when the total string length becomes n or greater


4. The final generated string is returned




---

#Example

Input:

10

Output:

12345678910


---
#Code

def task1():
    n = int(input("Enter the Position: "))
    s = ""
    i = 1

    while len(s) < n:
        s += str(i)
        i += 1

    return s

print(task1())


---
# Usage

Run the script using:

python filename.py

Enter the required position when prompted.


---

#Purpose

This program is useful for understanding:

1.String concatenation

2.Loops

3.Basic logic building

4.Sequence generation


#Task2 – Find the Number at a Given Position

This program determines which number appears at a specific position in the infinite sequence:

1234567891011121314...

You enter a position (e.g., 15), and the program calculates which number occupies that position.


---

Requirements

Python 3.x



---

Features

1. Reads a position pos from the user.


2. Builds a continuous number string starting from 1 until the string length reaches pos.


3. Then, iterates again to find exactly which number covers that position.


4. Prints the number found at the given position.




---

Setup

Create a file named task2.py in your project folder.


---

Code

def task2():
    pos = int(input("Enter position: "))
    s = ""
    n = 1

    # Step 1: Build the number string until its length reaches the given position
    while len(s) < pos:
        s += str(n)
        n += 1

    # Step 2: Find which number exists at the given position
    length = 0
    for i in range(1, n):
        new_str = str(i)
        length += len(new_str)

        # When cumulative length crosses or equals the position,
        # that number contains the desired position
        if length >= pos:
            print("Number at that position is:", i)
            break

task2()


---

Code Explanation

1. pos → User-input position in the infinite sequence.


2. s → A string that stores concatenated numbers ("1234567...").


3. First while loop → Builds the sequence until its length reaches the desired position.


4. Second loop (for) → Counts lengths of numbers one by one to find which number contains the target position

5. Once cumulative length ≥ pos, that number is printed as the answer.




---

Example

Input:

20

Sequence so far:
12345678910111213...

Output:

Number at that position is: 14
