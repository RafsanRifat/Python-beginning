letters = ["a", "b", "c", "d"]
letters[0] = "A"            # we can change a list item in this way
print(letters[0])           # This will return the first item of the list
print(letters[-1])          # This will return the last item of the list
print(letters[0:3])         # This will print the first three items of the list
print(letters[:3])          # This will also print first three items of the list. because by default python interpreter
                            # will indicate the free space as number 0.

print(letters[0:])          # This will print all the items of the list.
print(letters[:])           # same
print(letters[::3])         # only first and 3rd element will be printed .


numbers = list(range(20))
print(numbers[::2])         # eikhane sei sonkha guloi sudhu print hobe, jegulo ke 2 dara nissese bivajjo.
print(numbers[::-1])        # eikhane list er value gulo reverse akare decorate hobe
