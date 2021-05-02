from datetime import timedelta  # 2 ta time er moddhe parthokko repressent korte eita use kora hoy
from datetime import datetime

dt = datetime(2018, 1, 1)
dt2 = datetime.now()

time_duration = dt2 - dt
print(time_duration)

# this timedelta method has some methods =====>>>

print("days", time_duration.days)
print("seconds", time_duration.seconds)    # day chara baki j time gulo ache segulo k second a transfer kora
print("microseconds", time_duration.microseconds)
print("total_seconds", time_duration.total_seconds())  # total somoyer parthokko ke second a represent kore.
