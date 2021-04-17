
# Queues use kore FIFO =  First in First out method.
# [] list a amra jodi queue hisebe use kori sekhetre performance kom hoite pare karon--> prothom theke
# jokhon kono item remove kora hobe tokhon memoryte sob item gulo kei place change korte hoy, ei jonne eikhane Deque
# object use kora hoy.  Deque class/object  collecction namok Module theke import korte hoy.


from collections import deque

queue = deque([])    # eikhane deque object er moddhe diyea empty list list pass kora hoyeache, ei deque object er
                    # same method/behaviour list object er moto...

queue.append(1)
queue.append(2)
queue.append(3)

queue.popleft()
print(queue)

if not queue:           # jodi queue ta empty hoy
    print("Empty")