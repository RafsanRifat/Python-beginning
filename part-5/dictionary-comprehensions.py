values = []

for x in range(5):
    values.append(x * 2)

print(values)

values_2 = [x*2 for x in range(5)]   # uporer same kaj e kora holo list comprehension diyea.
print(values_2)


set_value = {x * 2 for x in range(5)}  # set comprehension... ... ...
print(set_value)

dictionary_value = {x: x*2 for x in range(5)}     # dictionary comprehension // x: is used here as key
print(dictionary_value)

rrr = {}
for r in range(5):
    rrr[r] = r * 2
print(rrr)


tuple_value = (x * 2 for x in range(5))   # Tuple er khatre comprehension use korte gele tuple ekta generator object
                                          # return korbe ... ... ...
print(tuple_value)

