from sys import getsizeof       # to know the size of an object



values = [x * 2 for x in range(100)]

print("List size : ", getsizeof(values))

# eikhane uporer code gulo te  list use kora hoiche... ...  R list er sob value memory te store hoy... jokhon onek boro
# kono data niyea kaj kora hobe , tokhon eto bisal dta memory te sobsomoy store na korte chaile, amaderke generator
# Expression use korte hobe. Karon generator Expression jei item gulo generate kore segulo konotai memory te save hoyna
# jar karone memory space kom lageee,,
# generator object use kora alada kichui na, just 3rd bracket er jayga te first bracket use kora... ... ...

values_2 = (x * 2 for x in range(100))

print("Generator size : ", getsizeof(values_2))
# generator object o iterable, we can loop over It, and in every Iteration we will get a new value from it.

# eikhane dekha jacche same  value howa sotteo list er size besi r generator object er size kom

#  Generator object sob kichu memory te store korena, jar karone--> pore generated data gulo access kora jayna.
# sudhu matro generate korar somoy e access kora jay... ... ... 