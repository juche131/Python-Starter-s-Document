import random
import string

print(random.random())  # 0.8063634671586678
print(random.randint(10, 20))  # 18
print(random.choice([2, 5, 9, 3, 5]))  # 5
print(random.choices([2, 5, 9, 3, ], k=2))  # [9, 2]
print(random.choices("qwertyuiopasdfghjklzxcvbnm", k=4))
# ['b', 'h', 'm', 'l']
print(",".join(random.choices("qwertyuiopasdfghjklzxcvbnm", k=4)))  # a,f,o,f
print(",".join(random.choices(string.ascii_letters, k=4)))  # f,l,q,B

print(string.ascii_uppercase)
print(string.digits)
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# 0123456789

numbers = [1, 9, 1, 9, 8, 1, 0]
random.shuffle(numbers)
print(numbers)  # [9, 9, 1, 8, 0, 1, 1]打乱排序
