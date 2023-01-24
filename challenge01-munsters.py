#!/usr/bin/python3
"""Alta3 Research | RZFeeser
   Review of Lists and Dictionaries"""

# define a short data set (in real world, we want to read this from a file or API)
munsters = {'endDate': 1966, 'startDate': 1964,\
        'names':['Lily', 'Herman', 'Grandpa', 'Eddie', 'Marilyn']}   # {} creates dict

# Your solution goes below this line
# ----------------------------------

# Display the value mapped to names
print("The value mapped to name is")
print(munsters["names"])

#display the endDate
print("endDate is")
print( munsters.get("endDate"))

#display the startDate
print("startDate is")
print( munsters.get("startDate"))

# print the value assoc with "endDate" key from the dict
#print(munsters["endDate"])  # should display 1966
print(munsters.get("endDate")) # does the same thing as line above, EXCEPT
                               # upon not finding a key, returns NONE instead
                               # of an ERROR

# print the value assoc with "startDate" key from the dict
#print("The Munsters began airing on:", munsters["startDate"])
print("The Munsters began airing on:", munsters.get("startDate"))

# print all names from the 3rd key

print("Characters on the Munsters include:", munsters.get("names"))

name = munsters["names"]
print(type(name))
print(name)

# create a simple for loop
for x in name: # if a line ends in a colon the next line Will be indented
    print(x, "is a character on the Munsters")
    print("---") #print 3 dashes on the screen each time through the loop

# we don't have to use a simple list to loop
# we could access the nested list within the dictionary->   munsters.get('name')
print("\nDisplays the same data, but by accessing the nested list within our dict\n")

for x in munsters.get("names"):
    print(x, "is a character on the Munsters")
    print("___")

# Add to the munsters
munsters["episodes"] = 70
print(munsters)
