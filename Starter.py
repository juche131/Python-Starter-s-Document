# Save Before Running!
# 库函数官方文档：：https://docs.python.org/3/library/
# 输出
from pprint import pprint
from sys import getsizeof
from array import array
from collections import deque
import math as m
print("Hello, world")
print("*" * 10)

# 布尔变量
Is_published = False
Is_published = True
false = False
TRUE = True

# 三引号
message = """
Hi, John,

This is a message from github.com.

Wish you a nice day.
"""
print(message)

# 字符串
course = "Python"
print(len(course))  # output = 6
print(course[0])
print(course[0:3])  # output = Pyt
print(course[1:])  # output = ython
print(course[:4])  # output = Pyth
print(course[-1])  # 倒数第一个字母 output = n

first = "Mosh"
last = "Hamedani"
full = first + " " + last
# f for format
full2 = f"{first} {last} \nNamelenth = {len(first) + len(last)}"
print(full + "\n" + full2)
'''
output = 
Mosh Hamedani
Mosh Hamedani
Namelenth = 12
'''

# Methods方法
course = "    Linear   alGebra      "
course_upper = course.upper()
course_lower = course.lower()
course_title = course.title()
course_strip = course.strip()
course_upper_location = course.upper
print(course_upper)
print(course_lower)
print(course_title)
print(course_strip)
print(course_upper_location)
'''output = 
    LINEAR   ALGEBRA
    linear   algebra
    Linear   Algebra
Linear   alGebra
<built-in method upper of str object at 0x000002E288CCAD30>
'''
course = course.lstrip()
print(course.find("al"))  # 13
print(course.find("12345"))  # -1
print(course.replace("a", "114514"))  # Line114514r   114514lGebr114514
ifLine = ("Line" in course)
ifNotSwift = ("Swift" not in course)
print(ifNotSwift)  # True
print(ifLine)  # True

# 运算以及复数的使用

z = 1+2j
print(f"{10 + 3} {10-3} {10*3} {10/3} {10//3} {10 % 3} {10**3}")
#        13       7      30 3.3333333333333335 3 1    1000


print(f"{round(2.9)} {abs(-2.9)} {m.ceil(2.2)}")

# Inputs输入
# x = input("x: ");
# print(type(x)); # <class 'str'>
# input始终返回str类型数据

# if-else

tempreture = 15
if tempreture > 30:
    print("It's hot")
    print("Drink waters")
elif tempreture < 10:
    print("It's cold")
else:
    print("It's nice!")
print("Done")

message = "Below 0" if tempreture < 0 else "Above 0"
# 简写，代码压缩术


print(message)

if tempreture >= -50 and tempreture < 50:  # same effect as -50 =< tempreture < 50
    print("Reasonable")
else:
    print("Unreasonable")
# and , or , not


# Loops 循环
Range = range(1, 4)  # 1,2,3
Range = range(1, 10)
print(type(Range))
for number in Range:
    print("Attempt", number)
    if number >= 10:
        print("End")
        break
else:
    print("did not reached 10")

for x in "Python":
    print(x)
# string , range, list is iterable which can used in a loop
# 可以迭代，可用于循环语句

sum = 0
number = 100
while number > 0:
    sum += number
    number //= 2
print(sum)

# functions 函数的自定义


# def greet():
#     print("Hi!\nWelcome Abroad!")
# 不能重载

def greet(firstName, lastName):
    print(f"Hello, {firstName} {lastName},\nWelcome abroad!")


greet("Mosh", "Hamedani")


def getGreeting(name="user"):

    return f"Hi {name}"


message = getGreeting(name="114514")
print(greet("Mosh", "Hamedani"))  # Hello...... None
print(message)
print(getGreeting())  # user


# 乱七八糟的用法
def multiply(*numbers):
    print(numbers)
    total = 1
    for num in numbers:
        total *= num
    return total


print(multiply(2, 3, 4, 5))  # (2, 3, 4, 5) \n 120


def saveUser(**user):  # A dictionary字典
    print(user)
    print(user["name"])


saveUser(id=1, name="John", age=22)
# select, shift+alt+Down to copy

# 数据结构 Data structure

# Lists
letters = ["a", "b", "c", "d", "e"]
matrix = [[0, 1], [2, 3], [4, 5]]
zeros = [0] * 10
combined = zeros + letters  # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'a', 'b', 'c']

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
numbers = list(range(20))
# ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
chars = list("Hello World")
print(matrix)
print(combined)
print(zeros)
print(numbers)
print(chars)
# index

print(letters[0:3])
print(letters[1:])
print(letters[::2])  # ['a', 'c', 'e']
# [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(numbers[::-1])
print(numbers[10:1:-2])  # [10, 8, 6, 4, 2]

number = [1, 2, 3]
first, second, third = number
# not this: first,second=number
number = list(range(6))
first, second, *other = number
print(other)  # [2,3,4,5]
first, *other, last = number
print(first, last, other)

for letter in enumerate(letters):
    print(letter)
    print(letter[0])

# Add items
letters.append("f")
letters.insert(1, "-")
print(letters)
# Remove
letters.pop()
print(letters)
letters.pop(1)
letters.remove("c")
del letters[3:4]
print(letters)

numbers = [3, 51, 2, 8, 6]
numbers.sort()
print(numbers)  # [2, 3, 6, 8, 51]
numbers.sort(reverse=True)  # [51, 8, 6, 3, 2]
print(numbers)

numbers = [3, 51, 2, 8, 6]
sortednum = sorted(numbers)
print(sortednum)

# ???神奇的功能
itemsScorce = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
    ("Product4", 8)
]
items = itemsScorce


def sortItem(item):
    return item[1]


items.sort(key=sortItem)  # 向sort操作中传递了一个函数
# [('Product4', 8), ('Product2', 9), ('Product1', 10), ('Product3', 12)]
print(items)

# another way to write it
items = itemsScorce
items.sort(key=lambda item: item[1])  # 利用lambda函数
print(items)  # 同上

# 提取值
items = itemsScorce
prices = []
for item in items:
    prices.append(item[1])
print(prices)  # [8, 9, 10, 12]
# Map function
x = map(lambda item: item[1], items)  # x is a class 'map' which is iterable
x = list(x)
print(x)  # [8, 9, 10, 12]

# filter function
# [('Product1', 10), ('Product3', 12)]
print(list(filter(lambda item: item[1] >= 10, items)))

# List comprihention
print([item[1] for item in items])  # [8, 9, 10, 12]
# [('Product1', 10), ('Product3', 12)]
print([item for item in items if item[1] >= 10])

list1 = [1, 2, 3]
list10 = [10, 20, 30]

# [('a', 1, 10), ('b', 2, 20), ('c', 3, 30)]
print(list(zip("abc", list1, list10)))

# stack 栈

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)
queue.popleft()
print(queue)
if not queue:
    print("Empty")


# 元组 touple
point = (1, 2)
point = (1, 2)+(3, 4)
point = (1, 2)*3

# touples could not be changed
# Invalid: point[0]=10
# Python Swapping based on touple:
x = 10
y = 11
x, y = y, x
print("x", x, "\ny", y)

# array: not easy to use
# Don't solve a problem that never exists: Only use array when encounterd performance problems
theArray = array("i", [1, 2, 3])  # i for signed integer
theArray[0]

# Set 集合（真的是集合）
numbers = [1, 9, 1, 9, 8, 1, 0]
first = set(numbers)
print(first)  # {8,1,9,0}
second = {1, 4}
second.add(5)
print(second)  # {1,4,5}
second.remove(4)
print(second)  # {1,5}

print(first | second)  # 并集Union{0,1,5,8,9}
print(first & second)  # 交集Intersection{1}
print(first - second)  # 差集Difference{8,9,0}
print(first ^ second)  # 环和Symettric Difference{8,9,5,0}

# first[0]is invalid:have no sequence 无序集
print(list(first))  # [8,1,9,0]
if 1 in first:
    print("1 in set", first)


# Dictionary 字典（一一对应）
point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
point["x"] = 10
point["z"] = 20
print(point)
print(point.get("a"))  # None
if "a" in point:
    1
del point["x"]  # {'y': 2, 'z': 20}
print(point)
# iterable
# for key in point.items():
#    print(key, point[key])???

# generator object
# e.g.
values = [x*2 for x in range(5)]
print(values)  # [0, 2, 4, 6, 8]
values = {x*2 for x in range(5)}
print(values)  # {0, 2, 4, 6, 8}
values = {x: x*2 for x in range(5)}
print(values)  # {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}
values = (x*2 for x in range(5))
print(values)  # <generator object <genexpr> at 0x00000242E4ACB1D0>
# Iterable
sum = 0
for i in values:
    sum += i

# Efficient: less Memory
values = (x*2 for x in range(1000000))
print("Memory use of genobj:", getsizeof(values))  # Memory use of genobj: 200
values = list(values)
print("Memory use of lists:", getsizeof(values))
# Memory use of lists: 8448728


# Unpacking Operator
print(numbers)  # [1, 9, 1, 9, 8, 1, 0]
print(*numbers)  # 1 9 1 9 8 1 0
values = [*range(5), *"hello"]
print(values)  # [0, 1, 2, 3, 4, 'h', 'e', 'l', 'l', 'o']

first = dict(x=1)
second = dict(x=10, y=2)
combined = {**first, **second, "z": 1}
print(combined)  # {'x': 10, 'y': 2, 'z': 1}

# excercise
sentence = "This is a common interview question"
char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
print(char_frequency)
pprint(char_frequency, width=1)  # Beautiful printing
print(sorted(char_frequency.items(), key=lambda kv: kv[1]))


# Error and Exception:
try:
    age = int(input("Age: "))
    xfactor = 10/age
except ValueError as eroor:
    print("You didn't enter a valid age.")
    print(eroor)  # Age: aggsy //invalid literal for int() with base 10: 'aggsy'
except ZeroDivisionError:
    print("Age should not be 0.")
else:
    print("No exceptions were thrown.")
finally:
    pass
print("Execution continues.")
# With satement:...
# Raise statement: 报错
