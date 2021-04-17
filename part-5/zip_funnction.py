# zip function use kora hoy, ek ba ekadhik iterable (list, string etc) ke ekti Tuple er list hisebe toiri korar jonno.

list1 = [1, 2, 3]
list2 = [11, 12, 13]

print(list(zip(list1, list2)))
# eikhane zip function ekti zip object return korbe (zip object iterable), sei object ke list a rupantor korar jonno
# list function use kora hoyeache.

print(list(zip("abc", list1, list2)))

# same vabe, eikhane string o use kora hoyeache.