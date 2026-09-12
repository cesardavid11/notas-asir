# collection = single "Vaeiable" used tp store multiple values

# List = [] ordered and changeable. Duplicates OK

fruits = ["banana", "apple", "orange"]

# set = {} unordered and immutable, but Add/Remove OK. No duplicates

objects = {"book", "phone", "spoon"}

# Tuple = () ordered and unchangeable. Duplicates OK. FASTER

pc_parts = ("CPU", "RAM", "Motherboard")



# A Checking Info & Searching

# len(fruits) : Retur the total number of items in the collection.
# Works on list, set and tupla.


# "pineapple" in fruits : Checks if an item exist inside the collection
# (return True on False). Extremely fast on sets.


# fruits.index("apple") : Returns the indes position of an items (list
# and tuples only).


# fruits.count("banana") : Counts how many times an items appears (list
# and tuples only).


# dir(fruits) : Prints all aviable methods and attributes associated
# with the object.



# B. Modifiying Collections (List Only)

# fruits.append("pineapple") : Adds an item to the end of the list.


# fruits.insert(0, "pineapple") : Inserts an item at the specific
# index (index 0 puts it at rhe beginning).


# fruits.remove("apple") : Removes the first occurrence the specified
# item.


# fruits.clear() : Empties the list completely.



# C. Rordering (List Only)

# fruits.sort() : Sorts the list in ascending order (alphabetical for
# strings, numerical for numbers).


# fruits.reverse() : Reverses the current order of elements in the list.