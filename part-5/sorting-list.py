numbers = [2, 3, 8, 77, 55, 88, 44]
numbers.sort()       # To sort a list in ascending order.....  eivabe sort korle list ta parmanently ascending/
                    # Drscrnding order a sort hoyea jay.  (sort method use kore sort kora hoyeache eikhane)
print(numbers)

numbers.sort(reverse=True)
print(numbers)             # To sort a list in Descending order


numbers_2 = [44,55, 25, 13, 66, 45, 78]
print(sorted(numbers_2))                    # evabe sort korle list ta sudhu ekhanei sort hoy, parmanently hoyna.
                                            # eikhane "osrted()" nammok builtin function use kore sort kora hoyeache.
print(sorted(numbers_2, reverse=True))
print(numbers_2)


#  example of sorting ------>

items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12)
]

def sort_item(item):
    return item[1]              # eikhane product gulor index "0" R price er index "1"

items.sort(key=sort_item)
print(items)

# print(sorted(items, key=sort_item))     ##   Eita diyeao same kaj hobe.

# eikhane items namok list k amra jodi sort method ba sorted function diyea sort kore sosori print kori, tahole
# python bujhte parena j kivabe sort korbe. karon ei items list er jei value/item gulo ache segulo protitai Tuple.
# ekhon eigoloke sort korte hoile Tuple er value guloke dhore sort korte hobe. Tuple er value gulor moddhe ekta name
# r ekta price ache. tai eikhane price k dhore sort korai best.   r ei jonno price er access dorkar.
# ei karone amra ekti customize function toiri korechi,  jei function  items list er protita item/value/Tuple er price
# return korbe. r sort method er moddhe sei customize function k key hisebe reffer koresi.
# ekhon sort method oi customize function er return kora price er upor depend kore sort korbe.
# iccha korle amra eikhane product er namer upore depend koreo sort korte parbo.---> sei khetre, price return na kore
# product name return korte hobe.


