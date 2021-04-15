# Lambda expression or Lambda function --->>    This is basically a simple oneline  Anonymous function, that we can
# pass to other function.  (orthat ei Lambda function k amra onno funciton a argument hisebe pass korte pari ba eitake
# sothik pass korao bujhayna, reffer kora type er kichu... ... ...   )

items = [
    ("product1", 10),
    ("product2", 9),
    ("product1", 12)
]

# def sort_item(item):
#     return  item[1]

items.sort(key=lambda items : items[1])   # Lambda function likhar dhoron holo---> lambda likhte hobe, tarpor-->
                                          #  parameter:expression    ...     tar mane holo---  prothome parameter
                                          # likhte hobe, r tarpor kolon er pore expression.
print(items)