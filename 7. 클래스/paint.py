from point import Point

def bound_class_method():
    p = Point()
    p.set_x(10)
    p.set_y(10)
    p.show()

def test_unbound_class_method():
    p = Point()
    Point.set_x(p, 20)
    Point.set_y(p, 20)
    Point.show(p)
    p.show()

def test_other_method():
    # print(Point.class_method(Point))
    print(Point.class_method())
    Point.static_method()


def main():
    # bound_class_method()
    # test_unbound_class_method()
    test_other_method()

if __name__ == '__main__':
    main()
