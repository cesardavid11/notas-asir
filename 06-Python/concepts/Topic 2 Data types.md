# Data types

**Date:** 2026-09-08
**Category:** (Python)

In Python, data types tell the computer what kind of value a variable is holding. This matters because Python treats different types of data differently—for example, adding two numbers together does math, but adding two pieces of text joins them together.

---

## 1. Numeric Data Types

Python offers several numeric data types to handle different kinds of numerical values.

1. **Integers (int):**

Whole numbers, positive or negative, without a fractional component. 

These are fundamental numeric values that represent counts or discrete measurements. 

Unlike floating-point numbers, integers are exact and do not involve approximations, making them ideal for scenarios where precision matters, such as indexing or counting items.

```
age = 25
```

2. **Floating-point numbers (float):**

Numbers with decimal points or in exponential form. 

These values are commonly used in fractional precision scenarios, such as financial calculations, scientific measurements, and graphics programming. 

Floating-point numbers can also represent extremely large or small values using exponential notation, making them versatile for various numerical applications.

```
price = 19.99
``` 

3. **Complex numbers (complex):**

Numbers with a real and imaginary part. Complex numbers are useful in fields like electrical engineering, physics, and signal processing, where operations involving imaginary numbers are common.

Python represents complex numbers as a + bj, where a is the real part, and b is the imaginary part. This built-in support simplifies calculations that would otherwise require external libraries or custom implementations in other languages.

```
z = 2 + 3j
```

## 2. Sequence Data Types

Beyond numbers, Python also provides sequence data types that store ordered collections of elements.

1. **Strings (str):**

Ordered sequences of characters enclosed in single or double quotes. Strings are one of the most versatile data types in Python, allowing you to store and manipulate text-based data. 

They are commonly used in tasks like handling user input, creating messages, or even processing large text datasets. 

Python provides a variety of built-in methods, such as .lower(), .upper(), .replace(), and .split(), that make working with strings highly efficient.

```
greeting = "Welcome to Python!"
```

2. Lists **(list):**

Lists are ordered, mutable collections of items, which can hold elements of different data types. 

This flexibility makes lists one of the most commonly used data types in Python, suitable for tasks ranging from simple storage to complex data manipulation. 

Lists allow dynamic resizing and support various operations such as slicing, appending, and removing elements, making them a go-to structure for scenarios requiring ordered and changeable data.

```
fruits = ["apple", "banana", "cherry"]
```

3. **Tuples (tuple):**

Ordered, immutable collections of items. Tuples are often used to store fixed collections of data where immutability is important, such as geographic coordinates, RGB color codes, or database records. 

Unlike lists, tuples cannot be modified after they are created, which makes them faster and more secure in scenarios where data integrity is critical.

```
dimensions = (1920, 1080)
```

## 3. Mapping Data Types

While sequences store ordered collections of elements, Python also provides mapping data types that associate keys with values. The most commonly used mapping type is the dictionary.

1. **Dictionaries (dict):**

Collections of key-value pairs, where keys are unique and immutable. 

Dictionaries are highly versatile and allow you to efficiently organize and retrieve data using meaningful keys rather than relying on numerical indexes. This makes them particularly useful for representing structured data, such as JSON objects or configuration settings. 

Python dictionaries also support various operations, such as adding, updating, or deleting key-value pairs, making them an essential tool in many programming scenarios.

```
person = {"name": "Alice", "age": 30}
```

## 4. Sets

In addition to sequences and mappings, Python provides set data types, which store collections of unique elements without a specific order.

1. **Sets (set):**

Unordered collections of unique elements. Sets are particularly useful when you need to ensure that your data contains no duplicates, such as in membership testing or removing duplicate entries from a list. 

They support mathematical operations like union, intersection, and difference, making them powerful tools for solving problems involving sets of data.

```
unique_numbers = {1, 2, 3, 4, 5}
```
2. **Frozen sets (frozenset):**

An immutable version of a set, which means that once created, its elements cannot be modified. 

Frozen sets are useful in scenarios where you need a hashable collection of unique items, such as using a set as a key in a dictionary or ensuring the integrity of data that should not change. 

They retain all the properties of regular sets, such as supporting mathematical operations like union and intersection, but with the added benefit of immutability.

```
immutable_set = frozenset([1, 2, 3])
```

## 5. Boolean Data Type

In many programming scenarios, we need a way to represent truth values. Python provides the Boolean data type, which plays a role in decision-making and control flow.

1. **Boolean:**

Logical values, either True or False. These values are often used in decision-making processes, such as conditional statements and loops. 

Booleans are fundamental to control flow in programming, allowing you to write code that reacts dynamically based on conditions. 

In Python, Boolean values can also result from comparisons (e.g., 5 > 3 evaluates to True) or logical operations (e.g., True and False evaluates to False).

```
is_active = True`
```

## 6. NoneType

In addition to numeric, sequence, mapping, set, and Boolean types, Python includes a special data type to represent the absence of a value.

1. **None (NoneType):**

Represents the absence of a value or a null value. 

The None type is often used to signify a placeholder, uninitialized variables, or the default return value of functions that do not explicitly return anything. 

It is useful, especially in cases where an operation might not produce a result or when a variable needs to be defined without an initial value.

```
result = None
```