# class point
class Point:
    count_of_instance = 0

    def set_x(self, x):
        self.x = x

    def get_x(self):
        return self.x

    def set_y(self, y):
        self.y = y

    def get_y(self):
        return self.y

    def show(self):
        print(f'점[{self.x}, {self.y}]를 그렸습니다.')

    @classmethod
    def class_method(cls):
        return cls.count_of_instance

    @staticmethod
    def static_method():
        print('static method called . . .')