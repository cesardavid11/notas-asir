# Conditionals if/elif/else

**Date:** 2026-09-09
**Category:** (Python)

Conditional statements let your code make decisions and execute different blocks of code depending on whether a condition is True or False.

In Python, the primary keywords for controlling flow are if, elif (short for "else if"), and else.

---

## 1. Syntax Overview

Python uses indentation (usually 4 spaces) to define which block of code belongs to which statement.

```
if condition1:
    # Runs if condition1 is True
elif condition2:
    # Runs if condition1 is False AND condition2 is True
else:
    # Runs if all conditions above are False
``` 


## The if Statement

The if statement is mandatory for any conditional check. It evaluates a boolean condition. If the condition is True, the indented block runs; if False, Python skips it.

```
temperature = 30

if temperature > 25:
    print("It's a hot day!")
```


## The elif Statement

elif allows you to check multiple conditions sequentially. Python checks elif statements only if the preceding if or elif conditions evaluated to False. You can have as many elif blocks as you need.

```
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
```

## The else Statement

The else statement acts as a catch-all fallback. It executes only if none of the preceding if or elif conditions were True. It is optional and can only appear once at the end.

```
age = 16

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")
```

## Key Rules & Tips

* Colon Mandatory: Always end your if, elif, and else lines with a colon (:).

* Indentation Matters: All code within a conditional block must be indented equally.

* Comparison Operators: Use == (equal to), != (not equal to), >, <, >=, and <= to build conditions.

* Logical Operators: Combine multiple conditions using and, or, and not:

```
if age >= 18 and has_license:
    print("You can drive.")
```    
