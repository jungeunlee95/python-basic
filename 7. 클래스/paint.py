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

def test_member():
    p = Point()
    p.set_x(30)
    p.set_y(30)
    print(f'{p.x}, {p.y}, {p.count_of_instance}, {Point.count_of_instance}')
    p.count_of_instance = 2000
    Point.count_of_instance = 3000
    print(f'{p.x}, {p.y}, {p.count_of_instance}, {Point.count_of_instance}')

def test_constructor():
    p1 = Point(10, 20)
    print(f'{p1.x}, {p1.y}, {p1.count_of_instance}, {Point.count_of_instance}')

    p2 = Point(10, 20)
    print(f'{p2.x}, {p2.y}, {p2.count_of_instance}, {Point.count_of_instance}')
    print(f'{p1.count_of_instance}')

    del p1
    print(f'{Point.count_of_instance}')

def test_to_string():
    p = Point()
    print(p)
    print(repr(p))

    p2 = eval(repr(p))
    print(p2)



def main():
    # bound_class_method()
    # test_unbound_class_method()
    # print('# 1 : ', end=' '); test_other_method()
    # test_member()
    # print('# 2 : ', end=' '); test_other_method()
    # test_constructor()
    test_to_string()

if __name__ == '__main__':
    main()
