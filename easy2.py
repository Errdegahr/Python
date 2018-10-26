# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить



def  lucky_ticket(ticket_number):
  ticket = str(ticket_number)
  t1 = ticket[:3]
  t2 = ticket[3:]
  sum1 = 0
  sum2 = 0
  for i in t1 :
    sum1 = sum1 + int(i)
  for i in t2 :
    sum2 = sum2 + int(i)
  if sum1 == sum2: return ('Удача')
  else: return ("Неудача")

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
