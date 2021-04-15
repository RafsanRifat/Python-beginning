def save_user(**user):  # parameter er agee jodi double star (**) use kora hoy, tokhon function a argument hisebe
                        # keyword argument pass korano jay--->nicher moto--->
    print(user)
    print(user["age"])  #user object er pore 3rd bracket er moddhe kono key likhle, sei key er value pete pari.
    print(user["id"])
    print(user["name"])


save_user(id=1, name="Asif", age="22")   #ei argument gulu function a dictionary type data hisebe pass hoy.
