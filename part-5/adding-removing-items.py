letters = ["a", "b", "c", "d"]

# Add items

letters.append("e")   # to add an item at the end of the list
print(letters)
letters.insert(0, "--")  # to add an item at the specifique position of the list.
print(letters)

# Remove items

letters.pop(1)   # to remove specifique index number item
print(letters)
letters.remove("b")  # to remove specifique item
print(letters)
del  letters[0:2]   # To delete a range number of items
print(letters)
letters.clear()     # To delete all items of the array
print(letters)