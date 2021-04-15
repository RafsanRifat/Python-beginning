# map function er kaj  holo transform kora. transform or map.
# map ekti builtin function. eitar 2ta parameters ache... prothom parameter ta holo--> ekti Function r 2nd parameter
# holo --> ek ba ekadhik iterable.
items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12)
]

prices = []
names = []

for item in items:
    prices.append(item[1])

print(f"Product prices ---> {prices}")
