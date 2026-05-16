# Importing libraries in python
import os
# from os import someSubModuleName

# Functions in python (No type required for arguments => python is dynamically typed)
def func1():
    # Declaring variables in python (no type required)
    x = 1
    x = "2"

    # Lists
    arr = []                    # empty list
    arr = [1, 2, 3]             # non-empty list with elements
    arr = [1, "pari", "sucks"]  # different data types

    # Lists can be mutated in python unlike arrays in Java
    arr = []

    # Adding elements
    print(f"Before: {arr}")
    arr.append(1)
    print(f"After: {arr}")

    print(f"Before: {arr}")
    arr.append(2)
    print(f"After: {arr}")

    print(f"Before: {arr}")
    arr.append(3)
    print(f"After: {arr}")

    # Removing elements
    print(f"Before: {arr}")
    arr.pop()
    print(f"After: {arr} [REMOVED FROM BACK]")

    print(f"Before: {arr}")
    arr.pop(0)
    print(f"After: {arr} [REMOVED FROM INDEX]")

def func2(x):
    return x + 1

# Driver code
if __name__ == '__main__':
    # Calling functions in python
    func1()

    # Some example code
    x = 1
    res = func2(x)
    print(f"Before, x = {x} and after, res = {res}")
