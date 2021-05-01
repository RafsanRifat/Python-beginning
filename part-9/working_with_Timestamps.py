import time

# print(time.time())  # time module has a method call time().   it returns the current date-time... It will return a
                    # floating point number. this floating point number represent the total number of second in the
                    # beginning of time.

def send_mail():
    for i in range(10000):
        print(i)

start = time.time()
send_mail()
end = time.time()

duration = end - start

print(duration)