try:
    file = open("exception-intro.py")   # kokhono kokhono kajer jonno amaderke file ba external kichu open korte hoy
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("you didn't enter a valid age")
else:
    print("No exception were thrown")
finally:                    # open kora file finally close korte hobe evabe, eivabe close korle kono exception thak r
                            # na thak, sei file/database/network-connection close hoyea jabe... ... ...
    file.close()