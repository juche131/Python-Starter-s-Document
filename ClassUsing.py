from abc import ABC, abstractmethod


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
print(combined)  # (8, 5)


#

class TagCloud:
    def __init__(self):
        self.__tags = {}
        # tags前面加下划线，代表该对象是私有的，不能被访问

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0)+1
        # 封装了一个词云统计器。

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)  # return a iterable object


cloud = TagCloud()
cloud.add("Python")
cloud.add("python")
cloud.add("Python")
cloud.add("PYthon")
cloud.add("PythOn")
cloud.add("C++")
cloud.add("C++")
cloud.add("c++")
print(cloud["python"])  #
try:
    print(cloud.__tags)
except AttributeError as error:
    print(error)
# 'TagCloud' object has no attribute '__tags'

# 没有完全意义上的私有成员：实际上可以访问，这只是一种防呆设计防止意外访问：
print(cloud._TagCloud__tags)  # {'python': 5, 'c++': 3}
# 有点麻烦~~~


class Product:
    def __init__(self, price):
        self.setPrice(price)

    def setPrice(self, value):
        if value < 0:
            raise ValueError("Price should not be negative.")
        self.__price = value


# product1 = Product(-50)
# Succesfully prevented the invalid value
# Not Pythonic

# Property?Decorator???


# Inheritance类的继承

class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")
# Animal:Parent:父类
# Mammal,Fish:Child:子类


class Mammal(Animal):

    """    def __init__(self):
        self.weight=2
        This will overwrite the __init in the Parent class and make .age unavailable
"""

    def __init__(self):
        print("Mammal Constructor")
        super().__init__()
        self.weight = 2
        # use this instead

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


fish1 = Fish()
print(fish1.age)
fish1.eat()  # 可以执行，因为fish继承了mammal中的Eat方法

# 事实上，所有类都继承了一个object的自带父类


def blahblahblah(object):
    pass


o = object()
print(issubclass(Mammal, object))  # True

# 利用类的继承自定义异常值


class InvalidOperationError(Exception):
    pass


# ？？？？

# 奇怪的操作，抽象类abstractmethod，多态，UIControl按下不表

# 可以修改Python默认类

class Text(str):
    def duplicate(self):
        return self + self


class TrackableList(list):
    def append(self, object):
        print("Append Called.")
        super().append(object)


list = TrackableList()
list.append("1")  # Append Called.
