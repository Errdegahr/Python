# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):

    if len(origin_list) > 1:
        pivot_index = len(origin_list) // 2
        smaller_items = []
        larger_items = []

        for i, val in enumerate(origin_list):
            if i != pivot_index:
                if val < origin_list[pivot_index]:
                    smaller_items.append(val)
                else:
                    larger_items.append(val)

        sort_to_max(smaller_items)
        sort_to_max(larger_items)
        origin_list[:] = smaller_items + [origin_list[pivot_index]] + larger_items

    return origin_list


print(sort_to_max([4, 12, -1, 1.4, 31, -31, 0, 5, 5]))