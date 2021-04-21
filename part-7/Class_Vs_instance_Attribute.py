# Python er object er attribute holo--> Dynamic,  ekta object er Attribute k j Constractor er moddhei define korte hobe
# amon na... class er bahireo proyojon onujayee object er attribute define kora jay, mane notun attribute add kora jay,
# amon ki ageer attribute keu update kora jay. Object er attribute gulo ke Instance attribute bola hoy.
# Object er attribute add ba update korar pashapashi Class er attributeo add/update kora jay.
# protita object er alada alada attribute thakte pare, kintu jeita Class er attribute, seita sob object er khetrei same.
# eikhane Attribute holo---> valu.


class Point:

    default_color = "Red"       # eita class attribute

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point  ({self.x}, {self.y})")

Point.default_color = "Yellow"    # eikhane class er bahire class attribute change kora holo... ... ...

poin = Point(10 , 20)
poin.draw()                     # ei value gulo holo instance attribute
print(poin.default_color)       # eita class attribute
print(Point.default_color)      # eita class attribute

another = Point(30, 40)
another.draw()                  # Instance attribute
print(another.default_color)    # Eita class attribute