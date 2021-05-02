import time
from  datetime import datetime


dt = datetime(2018, 1, 1)

current_dateTime = datetime.now()   # this is used for current date-time
print(current_dateTime)

converted_dateTime = datetime.strptime("2021/05/02", "%Y/%m/%d")   # this is used to convert string type date time into real date-time
print(converted_dateTime)     # https://docs.python.org/3/library/datetime.html   here is the documantation



converted_current_date_2 = datetime.fromtimestamp(time.time())    #  eivabe time.time() er total second ke present time
                                                                    # time a convert korte pari
print(converted_current_date_2)

print(current_dateTime.year)
print(current_dateTime.month)
print(current_dateTime.hour)


print(dt.strftime("%Y/%m")  )         # date-time ke string a rupantor korar jonno use kora hoy.



