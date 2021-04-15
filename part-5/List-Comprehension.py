items = [
    ("product1", 10),
    ("product1", 9),
    ("product1", 12)
]

prices = list(map(lambda item: item[1], items))
print(prices)
filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)

