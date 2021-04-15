for x in range(5):             # ---> the parent loop is called After loops
    for y in range(3):         # ---> And the child loops called inner loops
        print(f"({x}, {y})")