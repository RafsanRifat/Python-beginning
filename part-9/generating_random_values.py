import random
import string

print(random.random())                 # this random module has a method call random, that generate a float type random value

print(random.randint(1, 10))           # It generate a integer random value between two  numbers
print(random.choice([1, 2, 10, 4]))           # It will randomly pick one of the item of this array
print(random.choices([1, 2, 10, 4], k=3))           # It will randomly pick 3(according to the value of k) of the item of this array
                                                # it is useful to generate a random password.


#  Generating random password ============>>>

# print(random.choices("abcdefghijklmn", k=4))    # this will give  us an array of 4 character  randomly, but we need
                                                # random string.

# For this we need to do ======>
print("".join(random.choices("abcdefghijklmn", k=4)))    # we can add an empty string before it. that will join all the
                                                         # item of that array in a string



# kintu password generate er best way na eita.  jodi    "string" module import kora hoy, tahole ei string module er
# kichu attribute ache, jegulo useful...

print(string.ascii_letters)   #  this returnes a string, that includes all the uppercase and lowercase letters.
print(string.ascii_lowercase)  #  this returnes a string, that includes all the  lowercase letters.
print(string.ascii_uppercase)  #  this returnes a string, that includes all the  Uppercase letters.
print(string.digits)            # this will return 0-9 digits


# ekhon upore oivabe kichu string pass korar chaite ei string module er argument pass korle letters,capital,small,digit
# sob e pabe,  r perfect password generate hobe.

print("".join(random.choices(string.ascii_letters + string.digits, k=7)))

# aro perfect korar jonno sathe aro kichu add kora jete pare ====>>

print("".join(random.choices(string.ascii_letters + string.digits + "@#%&*", k=7)))


#   ekta array er items gulor order change korar jonno nicher poddhoti use kora hoy =====>>

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)
