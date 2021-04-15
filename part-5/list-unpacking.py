# Amara ekti list er item guloke ekti ba ekadhik variable a assign kore rakhte pari (we can assign the elements of
#  a list into variables, this is called list unpacking).

numbers = [1, 2, 3]

first = numbers[0]
second = numbers[1]
third = numbers[2]

# ei kaj ti amra aro sohoj r clean vabe korte pari------>

first, second, third = numbers


numbers_2 = [4, 5, 6, 7, 8, 9]

first_item, second_item, *other = numbers_2
print(first_item)
print(second_item)
print(other)

# list unpacking er somoy, protita items kei variable a assign korte hobe, tachara koono variable assign korlam, abar
#  konota korlamna, eirokom kichu hoile error show korbe. jodi sob items k alada alada variable a assign korar dorkar
# na hoy tashole  jeguloke variable a assign kora dorkar seguloke assign kore niyea, baki sob guloke onno ekti
# variable a assign kore rakhte hobe (Ashole onno ekti variable a na , mainly eita onno ekta alada list a rakha hocche
#   r sei alada list ta ke amra agee star symble diyea define kore dicchi),
# r obossoy tar agee star mark dite hobe....    upore prothon 2 item chara baki
# sob gulo ke *other variable a assign kore rakha hoyeache.

numbers_3 = [112, 223, 445, 5566, 776, 556]
first_one, *other_items, last_one = numbers_3
print(first_one)
print(other_items)
print(last_one)

# eikhane prothom r ses item k variable a assign kora hoyeache. r majher baki sob guloke ekti alada variable a assign
# kore rakha hoyeache... 