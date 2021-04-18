numbers = [1, 2, 3, 4]

print(*numbers)   # object er namer agee * diyea prefix kore amra operator k unpacking korte pari...


values = list(range(5))
print(*values)

values_2 = [*range(5), *"Hello"]    # we can any Iterable using * before that Iterable
print(values_2)


first = [1, 2]
second = [2, 3]
combined_list = [*first, *second]   # we can combined 2 list using this.
print(combined_list)

first_dix = {"x": 1}
second_dix = {"y": 2, "x": 10}

combined_dix = {**first_dix, **second_dix} # we can combined 2 dictionary using this, but here need 2 **.
                                           # same key thakle last key sudhu dhorbe eikhane. 
print(combined_dix)

