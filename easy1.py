__author__ = 'Розов Сергей Алексеевич'

fruits = ['Груша', 'Киви', 'Банан', 'Яблоко', 'Абрикос', 'Апельсин']

for num, frut in enumerate (fruits):
    print (str(num) + '.  {:>8}'.format(frut))