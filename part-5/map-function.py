# map function er kaj  holo transform kora. transform or map.
# map ekti builtin function. eitar 2ta parameters ache... prothom parameter ta holo--> ekti Function r 2nd parameter
# holo --> ek ba ekadhik iterable.

items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12)
]

# prices = []
# names = []
#
# for item in items:
#     prices.append(item[1])
#
# print(f"Product prices ---> {prices}")

# x = map(lambda item: item[1], items)
# eikhane ei map function ti er vetorer lambda function ke items namok list er protita item er upore apply korbe.
# ei map function items namok itarable er protita item er upore itarate korbe, r ei itarate korar somoy, prottek bar
# ei lambda function ke call korbe...  r tokhon ei lambda function er item namok parameter diyea items namok iterable
# er protita item pass hobe, r ei lambda function ta return korbe item[1] ,,,,  orthat pass howa item er 1 num index
# orthat price. eikhane jodi item[0] return kortam tahole item name return korto.
# ekhon map function tar vetorer iterable er protita items er upore iterate kora ses hoile ekta iterable map object
# return korbe.
# ekhon ei map object k iterate korle orthat loop chalaile price gulo pabo.
# price gulo ke list akare pete hoile  amaderke ei map object k list object a transform korte hobe. list object a
# transfer korar jonno list function use korte hobe. karon amra jani j list function j kono iterable object k list
#  object a transform kore. r eikhane jehetu map object o iterable, tai list function eke list object atransform
# korbe...
# ============================================

# print(x)
# for item in x:
#     print(item)

# using map function --->>
prices = list(map(lambda item: item[1], items))
print(prices)



