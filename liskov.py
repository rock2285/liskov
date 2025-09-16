# shapes################################################
class Rectangle:
    def __init__(self, l=1, w=1):
        self.length = l
        self.width = w

    def setLength(self, n):
        self.length = n

    def getLength(self):
        return self.length

    def getWidth(self):
        return self.width

    def setWidth(self, n):
        self.width = n

    def area(self):
        return self.width * self.length


class Square(Rectangle):
    def __init__(self, length=1, width=1):
        # width is never used, but method matches signature of parent's init
        self.length = length
        self.width = length

    def setLength(self, n):
        self.length = n
        self.width = n

    def setWidth(self, n):
        self.width = n
        self.length = n


# main#############################################

def measure(s):
    print(s.getWidth(), "x", s.getLength())
    print("Area:", s.area())

    print("double length...")
    s.setLength(2 * s.getLength())

    print(s.getWidth(), "x", s.getLength())
    print("Area:", s.area())


a = Square(6)
b = Rectangle(8, 3)

print("\nsquare")
measure(a)
print("\nrectangle")
measure(b)