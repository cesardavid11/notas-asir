# for loops and while loops

**Date:** 2026-09-10
**Category:** (Python)

A for loop in Python iterates over the items of any sequence (such as a list, tuple, dictionary, set, or string) or an iterable object, executing a block of code for each item in order.

--- 

## Basic Syntax

```
for item in sequence:
    # Code block executed for each item
```

* **item:** A variable name you assign that holds the current element during each iteration.

* **sequence:** The collection or iterable object you are stepping through.

## Key Usage Examples

1. Iterating Over a List or String

```
# Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterating over a string
for char in "Python":
    print(char)
```

2. Using range() for Repeating Code

To run a loop a specific number of times, use the built-in range() function.

```
# Prints 0 through 4 (stops before 5)
for i in range(5):
    print(i)

# range(start, stop, step) -> Prints 2, 4, 6, 8
for i in range(2, 10, 2):
    print(i)
```

3. Accessing Index and Value (enumerate)

When you need both the index position and the item value, wrap the iterable in enumerate().

```
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"Index {index}: {color}")
```

4. Iterating Over Dictionaries

By default, looping over a dictionary iterates through its keys. You can specify .values() or .items() to access values or key-value pairs.

```
person = {"name": "Alice", "age": 30}

# Iterating through key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")
```


## Loop Control Statements

* **break:** Exits the loop immediately.

* **continue:** Skips the remainder of the current iteration and moves to the next item.

* **else:** An optional block that executes only if the loop completes normally without encountering a break.

```
# Example of break and else
for number in range(1, 10):
    if number == 5:
        break  # Loop ends early when number reaches 5
    print(number)
else:
    print("Loop finished completely!") # This will NOT print due to the break
```