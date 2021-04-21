# Method 3 dhoroner hoy---> Instance method, Class method, Static method.
# Instance method --->> ei method use hoy class er instance(object) er khetre.
# Class method --->> sob instance e eita use korte pare.
# Static method ---> eita independent method, r eita te kono parameter er dorkar hoyna.

# Class Method r Static method er khetre  decorator use korte hoy. na use korle error show kore... 
class Point:

    default_color = "Red"

    def __init__(self, x, y):           # eigulo instance method
        self.x = x
        self.y = y

    @classmethod   # eitake decorator bola hoy
    def zero(cls):          # eivabe class method define kora hoy
        return cls(0, 0)

    def draw(self):                         # eigulo instance method
        print(f"Point  ({self.x}, {self.y})")

Point.default_color = "Yellow"

poin = Point(10 , 20)
poin.draw()
print(poin.default_color)
print(Point.default_color)

another = Point(30, 40)
another.draw()
print(another.default_color)

point = Point.zero()
point.draw()