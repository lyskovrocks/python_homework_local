"""
В данной программе указывается количество часов, которые отработал человек в неделю
Программа должна расчитать сколько человеку должна быть оплата
Для проверки 50 часов 30900 рублей
"""

hours = int(input('Введите количество отработанных часов: '))
standart_hours = 40      # стандартное количество часов в неделю
standart_hour_pay = 600  # оплата в рублях в час
over_percent = 15        # повышение стандартной ставки
result_pay = 0           # результат, куда нужно записать итоговую оплату в неделю
# Вставьте сюда недостающий блок кода
#           |
#           V
over_percent = over_percent / 100 + 1
if hours <= 40:
    result_pay = hours * standart_hour_pay
else:
    result_pay = standart_hours * standart_hour_pay + (hours - standart_hours) * standart_hour_pay * over_percent

#  -----------------------------------
print(f"Работнику необходимо оплатить {result_pay} рублей.")