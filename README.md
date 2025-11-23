📘 Task1 – Number Sequence Generator

This project contains a simple Python program that generates a continuous sequence of natural numbers (like "12345678910...") until the total length reaches the user-given position.


---

🚀 How It Works

1. The user enters a number n


2. The program keeps appending numbers starting from 1 ("1", "2", "3", …)


3. It stops only when the total string length becomes n or greater


4. The final generated string is returned




---

🧾 Example

Input:

10

Output:

12345678910


---
🛠 Code

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

📌 Usage

Run the script using:

python filename.py

Enter the required position when prompted.


---

📄 Purpose

This program is useful for understanding:

String concatenation

Loops

Basic logic building

Sequence generation
