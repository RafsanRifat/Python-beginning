items = [
    ("product1", 10),
    ("product1", 9),
    ("product1", 12)
]

prices = list(map(lambda item: item[1], items))
print(prices)
# ei mapping tai comprehensions a korte hoile --- >>
comprehension_price = [item[1] for item in items]
print(comprehension_price)
filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)
# ei mapping tai comprehensions a korte hoile --- >>
comprehension_filter = [item for item in items if item[1] >= 10]
print(comprehension_filter)
# eikhane items er upore for loop cholteche, cholar somoy, protita item er upore if statement proyog hocche. r jei item
# gulo sob sorto mene true hocche, sei item guloi ekdom bamer item a ese store hocche, ba true howa item gulo ke
# ekdom bamer otem er kache return kora hocche.





# map abong filtering er kaj amra onno ekti upayea korte pari... seti e hocche comprehensions . list comprehensions er
# structure hoilo --->  [Expression for item in items]
# (personal montobbo--> Expresseion er jaygai seita thakbe, jeita amra chacchi ei list comprehensions theke).
#
