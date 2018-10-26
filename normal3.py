# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def myFilter(func, iterated):
    return (item for item in iterated if func(item))
print(list(myFilter(lambda x: True if x % 2 == 0 else False, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))