# Set is a collection of no Duplicate data.

numbers = [1, 1, 2, 2, 3, 4, 5]  # eikhane kichu duplicate item ache, mane eki item ekadikbar. ei duplicate gulo remove
                                 # er jonno set use kora hoy.


uniques = set(numbers)
print(uniques)

# output a kheyal korle dekha jabe j set item gulo second bracket er moddhe ache. sei item gulo likhte {} use kora hoy.

second = {5, 8}   # set eo list er moto korei item add ba remove kora jay.
print(uniques | second)  # 2 set er union kora holo eikhane
print(uniques & second)  # Intersection kora holo eikhen
print(uniques - second)  # difference between two sets
print(uniques ^ second) # symmetric of two sets.  mane --> jei item gulo 2ta te common nei.



# set holo ekta unorder list, eikarone amra set er kono item er index number dhore access paina. orthat
# print(second[1])  # eikhane error dibe.

# kintu amra check korte pari j kono item oi set er moddhe ache kina.

if 5 in second:
    print("yes")