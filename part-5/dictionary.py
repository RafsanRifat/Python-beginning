# In python dictionary is a collection of key value ,
# for example : phonebook..  Name ---> number.   eikhane name holo key r value holo number.


point = {"x": 1, "y": 2}  # eita dictionary define er ekta way. eikhane x r y hocche key r 1,2 hocche value.

# dict function use koreo dictionary define kora jay, tokhon r string k  coutation er moddha rakhte hoyna, colon o
# use korte hoyna. dict function er moddhe keyword argument use kora jay.

point_2 = dict(r=3, j=5, y=7)
print(point_2)
print(point_2["r"])  # kono index er value pete chaile sei index er name evabe likhte hobe. index number diyea list er
                     # moto kore value pawa jabena. here name of the key is index.

point_2["r"] = 10    # to change a value
point_2["j"] = 20
point_2["q"] = 30    # to add a new value

if "a" in point_2:
    print(point_2["a"]) # jei item list a nai, sei item print korte chaile type error dibe, error solve er jonno er agee if
                    # use kora jay, othoba .get() method use kora jay. ekhetre get use korai best.

print(point_2.get("a"))  # ei khetre none print hobe... othoba eikhane a er pore coma diyea ja likhe dewa hobe, setai
                         # print hobe none er jayga te.

del point_2["r"]        # to delete an item

#### ========================================================================================

# we can loop over a dictionary.

for key in point_2:
    print(key, point_2[key])

# we can loop over dictionary using .items() method --- >>
for key in point_2.items():    # this will return a tuple. we have to unpack the tuple
    print(key)

for key, value in point_2.items(): # eikhane tuple k unpack kora hoyeache...
    print(key, value)

# print(point_2)