# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {"VENEZUELA": "CARACAS",
            "ESPAÑA": "MADRID",
            "USA": "WASHINGTON D.C.",
            "CHINA": "BEIJING"}


# Accessing & Reading Data

# capitals.get("VENEZUELA") : Safely retrives the value asscociated with
# the key "VENEZUELA" (returns "CARACAS").


# Adding & Updating Data

# capitals.update({"PERU": "LIMA"}) : Adds a new key-value pair if the
# key doesn't exist, or updates the existing value if the key is already present.


# Removing Data 

# capitals.pop("CHINA") : REmoves the key "CHINA" (and its value "BEIJING")
# from the dictionary. it also returns the removed value ("BEIJING").


# Extracting Pars of a Dictionary

# capitals.keys() : Returns a dynamic viuw of all the keys in the dictionary
# (dict_keys(['VENEZUELA', 'ESPAÑA', 'USA', 'CHINA'])).


# capitals.values() : Returns a dynamic view of all the values in the dictionary
# (dict_values(['CARACAS', 'MADRID', 'WASHINGTON D.C.', 'MOSCOW'])).

# capitals.items(): Returns pairs of (key, value) tuples. Extremely useful for looping:

for country, capital in capitals.items():
    print(f"The capital of {country} is {capital}")