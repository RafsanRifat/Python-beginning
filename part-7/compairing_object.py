class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

poin = Point(1, 2)
other = Point(1, 2)

print(poin == other)  # eikhane 2tar value same howa sotteo false ashteche, karon---> eikhane Python interpretor 2ta
                      # 2ta object er address er compare korteche, value er na. jehetu 2 ta object er address alada,
                      # tai false ashteche.

print(poin > other)   #eikhane error show korbe, bolbe j poin r other, 2tai point er object,  ei karone 2tar compare
                      # kora jabena. ei problem solve er jonno --->> __gt__ magic method use korte hobe. er o 2ta
                      # parameter use kora hoy. ekta self, arekta other. python auto less than o implement kore nibe.
print("poin = ", id(poin))
print("other = ", id(other))

# ei problem solve korar jonno amaderke ekta magic method use korte hobe.  __eq__  ,  r eitar 2ta parameter ache.
# ekta holo --->> self, arekta other.    tahole value guloi compare korbe, address na.


