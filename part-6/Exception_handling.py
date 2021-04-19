try:
    age = int(input("Age: "))   # to handle the Exception we need to put the exception in a try block.
except ValueError:             # keu int chara onno type er input dile value error show kore, sei value error theke
                               # bachar jonno ei exception ...
    print("You didn't enter a valid age")
else:
    print("No exception were thrown")   # eikhane iccha korle else o use kora jay. jodi user sothik input dey, tahole
                                        # else kaj korbe, na hoile korbena.