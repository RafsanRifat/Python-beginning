# Amra jokhon kono function toirir somoy nirdisto sonkhok parameter  dibo, tokhon argument pass korar somoy o thik oi
# sonkhok e argument pass koraite parbo. ekhon jodi amra iccha moto besi poriman argument pass koraite chai, tahole-
# parameter hisebe ekta parameter nibo(word ta plural hoile valo), r tar agee ekta star dibo. tahole amra  multiple ba
# iccha moto argument pass koraite parbo.


# ---->> ekhon jei argument gula pass korabo, segula tuple hisebe ashe  function a ashe. orthat eivabe------>>
# (2, 3, 5, 6, 7) ...  tuple onekta  list er motoi, tuple o iterable.  kintu parthokko holo--->> list 3rd brkt thake
# r tuple a 1st brkt thake. list a  value insert ba delete kora jay, kintu tuple a ta jayna.


def multiply(*numbers):
    total = 1
    for number in numbers:
        # total = total * number
        total *= number
    return total


# print(multiply(1, 2, 3, 4, 5, 6))
value = multiply(1, 2, 3, 4, 5, 6)

print(value)