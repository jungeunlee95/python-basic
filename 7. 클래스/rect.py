# class rect

class Rect():

    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "Rect({0}, {1}, {2}, {3})".format(self.x1, self.y1, self.x2, self.y2)

    def area(self):
        return (self.x2 - self.x1) * (self.y2 - self.y1)

    def draw(self):
        print("{0}를 그렸습니다.".format(self))


def test_class_rect():
    r1 = Rect(10, 10, 50, 50)
    r2 = eval(repr(r1))

    print(r1, str(r1.area()), sep=':')
    print(r2, str(r2.area()), sep=':')

    r1.draw()
    r2.draw()

test_class_rect()