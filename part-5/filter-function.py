# nicher list ta ke amra filter korbo. eikhane jei product gulor price 10 ba 10 er upore sudhu seguloi print korbo.
items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12)
]

# eita amra nicher way te korte pari--- >

# prices = []
# for item in items:
#    if item[1] >= 10:
#        prices.append(item)
# print(prices)


# Abar eita filter() function use koreo korte pari...

filtered_items = (list(filter(lambda item: item[1] >= 10, items)))

print(filtered_items)

# filter function o map function er moto korei kaj kore... eikhane 2ta parameter thake filter function a. prothom
# parameter holo function r 2nd function holo iterable. eikhane prothom a ekti lambda function use kora hoiche.
# jar parameter holo- item, r tar pore bola hoiche j jesob item[1]  er value 10 er soman ba tar chaite boro, sesob
# item gulo return korbe.
# map function er moto ei filter function o same type iterable object return kore. tarpor sei iterable object k list
# function dara list object kore newa hoyeache.
