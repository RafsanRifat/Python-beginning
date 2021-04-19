# we can raise our own Exception
def calculate_xfactor(age):
    if age <=0:
        raise ValueError("Age cannot be 0 or less")  # eikhane amra error message  specify korte pari... ... ...
    return 10 / age

try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)