# there is a heap memory in our computer, all the obj is stored there.   r protita object er address thake.
#   id() function er maddhome amra kono object er address jante pari
# __init__ use kore constructor toiri korte hoy. t constructor toiri kora hoy, bahire theke input newar jonno ba,
# vetorei fixed input define er jonno.
# (self) current object k define kore ba bujhay, mane bortomane jei object niyea kaj hocche, sei object k bujhay


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        print(f"poin ({self.x}, {self.y})")



poin = Point(10, 20)
poin.draw()