#   Functions

**Date:** 2026-09-10
**Category:** (Python)

A function in Python is a reusable block of code that performs a specific task. Functions help organize code into logical sections, avoid repetition, and make programs easier to debug and maintain.

---

## Basic Syntax

Functions are defined using the *def* keyword, followed by the function name, parentheses (), and a colon :.

```
def function_name(parameters):
    """Optional docstring explaining what the function does."""
    # Code block
    return result  # Optional return statement
```

## Key Concepts & Examples

1. Defining and Calling a Function

To use a function, define it first, then "call" (execute) it by its name followed by parentheses.

```
def greet():
    print("Hello, welcome to Python!")

# Calling the function
greet()
```

2. Passing Parameters and Arguments

Parameters allow you to pass data into a function.

```
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Alice")  # Output: Hello, Alice!
```

3. Default Parameter Values

You can set default values for parameters. If an argument isn't provided during the function call, the default is used.

def greet_with_title(name, title="User"):
    print(f"Hello, {title} {name}!")

```
greet_with_title("Bob")           # Output: Hello, User Bob!
greet_with_title("Alice", "Dr.")  # Output: Hello, Dr. Alice!
```

4. Returning Values (return)

Functions can pass results back to the caller using the *return* statement. Once a *return* statement is executed, the function stops running immediately.

```
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(result)  # Output: 8
```

> Note: If a function does not explicitly use a return statement, it automatically returns None.ç

5. Flexible Arguments (*args and **kwargs)

When you don't know in advance how many arguments will be passed:

* *args: Collects positional arguments into a tuple.

* **kwargs: Collects keyword arguments (key-value pairs) into a dictionary.

```
# *args example
def calculate_sum(*numbers):
    return sum(numbers)

print(calculate_sum(1, 2, 3, 4))  # Output: 10

# **kwargs example
def print_user_profile(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

print_user_profile(name="Sam", role="Developer", status="Active")
```

6. Lambda (Anonymous) Functions

For short, single-expression functions, Python supports inline lambda functions.

```
# Standard function
def square(x):
    return x ** 2

# Equivalent lambda function
square_lambda = lambda x: x ** 2

print(square_lambda(4))  # Output: 16
``