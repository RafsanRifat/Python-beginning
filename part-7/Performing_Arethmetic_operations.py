class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # def __eq__(self, other):
    #     return self.x == other.x and self.y == other.y
    # def __gt__(self, other):
    #     return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return self.x + other.x and self.y + other.y


poin = Point(1, 2)
other = Point(1, 2)


print(poin + other)  # add korte chaile error asbe, eita solve er jonno--->> __add__ magic method use korte hobe.