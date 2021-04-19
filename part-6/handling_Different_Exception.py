try:
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):  # ekadhik exception er somvabona thakle, segulo ek line ei include kora jay.
    print("You didn't enter a valid age")
else:
    print("No exception were thrown")