try:
    with open("exception-intro.py") as file:
        print("file opened.")    # ei block a amra ei file k niyea kaj korte parbo. amra jokhon with open call korbo,
                                 # Tokhon, python automatically file.close() k call korbe, r  kaj sese close kore
                                 # dibe, tahole r amader finslly: file.close()  korar dorkar nai...

# (file.__exit)(file.__enter) jesob file er ei 2ta magic method ache, sei file gulote with use kora jay.

    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("you didn't enter a valid age")
else:
    print("No exception were thrown")
