# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

mass = [2, 4, 6, 8, 10, 12, 9];
list = list(num for num in mass if (num % 3 == 0 and num > 0 and num % 4 != 0));
print(list);