from timeit import timeit    # it will use to calculate the execution time of a python code


def calculate_xfactor(age):
    if age <=0:
        raise ValueError("Age cannot be 0 or less")  # eikhane amra error message  specify korte pari... ... ...
    return 10 / age

try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)



# raise exception use na korai better. jodi ekantoi korte hoy, tokhon korte hobe... ... ...