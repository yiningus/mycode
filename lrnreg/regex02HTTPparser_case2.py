import re

searches= []
print(f"Great! Please enter a string to search for:")

while True:
    searchFor = input("> ")
    if searchFor.lower() == "quit":
        break
    searches.append(searchFor)
    print("Type in another string to search for, or type QUIT to continue:")
    for search in searches:
        count= re.findall(search.lower(), searchMe.lower())
        print(f"Total occurrences of {search}: {count}")
