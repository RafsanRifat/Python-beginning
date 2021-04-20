# class toiri korar somoy, protita method er moddhe self thakbe parameter hisebe.
class Point:
    def draw(self):
        print("draw")


pointtt = Point()   # eikhane pointtt ke Point() class er object hisebe define kora holo.

print(type(pointtt))  # pointt object kon class er object ta check kora holo, othoba, kon typer object, ta check kra hlo
print(isinstance(pointtt, Point))  # isinstance() function er maddhome kono object ekti function er  instance kina , ta
                                   # jana jay. instance hoile value true, r instance na hoile value false.