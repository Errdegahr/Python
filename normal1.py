# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):

    x, y = 1, 1
    f_list = [1, ]

    for i in range(m):
        x, y = y, y + x
        f_list.append(x)

    return f_list[n - 1:m]


print('Ряд фибоначи(1, 10): ', fibonacci(1, 10))