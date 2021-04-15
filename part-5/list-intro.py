# in python there may have different types of datatypes in one list
letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]
zeros = [0] * 10          # we can use * to repeat  the items in the list. (not multiplying)
print(zeros)

combined = letters + zeros  # we use + to combaine two list. (not sumation)
print(combined)


new_list = list(range(20))  # list function er kaj holo jkono iterable k list a rupantor kora. eikhane range function
                            # holo iterable.


print(f"Here items = {len(new_list)} And the list is in below: \n  {new_list} ")

char = list("Hello world!!!")
print(char)
