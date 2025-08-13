class Point:
    def __init__(self, x, y):  # 构造函数
        self.x = x
        self.y = y
    # https://rszalski.github.io/magicmethods/#operators

    def __str__(self):  # Magic method for string representation
        # __str__ is called when print() is used on the object

        return f"({self.x}, {self.y})"  # 自定义运算符？

    def __eq__(self, other):  # Magic method for equality comparison
        return self.x == other.x and self.y == other.y

    def __add__(self, other):  # Magic method for addition
        return Point(self.x + other.x, self.y + other.y)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point1 = Point(1, 2)  # 定义point
print(type(point1))  # <class '__main__.Point'>
print(isinstance(point1, Point))  # True
print(isinstance(point1, int))  # False
print(point1.x)
point1.draw()  # Point (1, 2)
print(point1)  # 调用__str__方法，输出 (1, 2)
print(str(point1))  # 自定义__str__方法后，直接打印point1会调用该方法

point1 = Point(3, 4)
point2 = Point(3, 4)
print(point1 == point2)  # 定义__eq__方法前，比较的是地址，返回False
# 定义__eq__方法后，比较的是x和y的值

point2 = Point(5, 1)
combined = point1 + point2  # 定义了__add__方法
print(combined)  # 8 5
