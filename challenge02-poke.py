#!/usr/bin/python3
"""Alta3 Research | RZFeeser
   For Loop Example - Create for loop to work across the dataset provided"""

print("Welcome to the PokeAPI data parser")

# dataSet is JSON adapted from https://PokeAPI.co
dataSet = [{"ability": {"name": "static", "attack type": "electric"}, "is_hidden": False, "slot":1}, {"ability": {"name": "lightning-rod", "attack type": "electric"}, "is_hidden": True, "slot": 3}]

# Finish the code below this line
# -------------------------------

# use a for loop to display all abilities
for ability in dataSet:
    print(ability)

print()
# use a for loop to display JUST the details of a single ability
for ability in dataSet:
    print(ability.get("ability"))

print()

# use a for loop to display JUST the names of a single ability
for ability in dataSet:
    print(ability.get("ability").get("name"))
