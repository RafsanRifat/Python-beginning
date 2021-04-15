letters = ["a", "b", "c"]

# for letter in letters:
#     print(letter)


for index, letter in enumerate(letters):    # eikhane amra protita item er index number pawar jonno enumerate() ei built in
                                    # funciton use korechi. r eti ekti enumerate object return korbe. ja Iterable.
                                    # prottek Iteration a eti ekti 2 item er tuple return korbe. jeikhene prothom
                                    # item ta holo index, r 2nd item ta oi index er item.
                                    # for er pore 2ta variable use kore amra sei Tuple k unpack kore nite pari.
                                    # r tarpor segulo ke print korte pari.
    print(index, letter)


