n = None
try:
    n = int(input('Введите целое, положительное число: '))
except BaseException as e:
    print('Необходимо ввести целое, положительное число')
    exit()
sum = 0
for i in range(n+1):
    if i % 3 == 0 or i % 5 == 0:
        if i % 3 == 0 and i % 5 == 0:       # Ищем число кратные и 3 и 5
            sum = sum + i*2
        else:
            sum = sum + i
print(f'Сумма чисел кратных 3 и 5 равна {sum}')

#======================================================================================================================






