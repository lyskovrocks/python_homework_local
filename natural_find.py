# n = None
# try:
#     n = int(input('Введите целое, положительное число: '))
# except BaseException as e:
#     print('Необходимо ввести целое, положительное число')
#     exit()
# sum = 0
# for i in range(n+1):
#     if i % 3 == 0 or i % 5 == 0:
#         if i % 3 == 0 and i % 5 == 0:       # Ищем число кратные и 3 и 5
#             sum = sum + i*2
#         else:
#             sum = sum + i
# print(f'Сумма чисел кратных 3 и 5 равна {sum}')

#======================================================================================================================
ask = 'y'
n = None
for _ in range(1000):
    if ask == 'y':
        err = 0
        for i in range(3):
            try:
                # n = -q
                n = int(input('Введите целое, положительное число: '))
            except BaseException as e:
                print('Необходимо ввести ЧИСЛО')

                if n <= 0:
                    print('Необходимо ввести ПОЛОЖИТЕЛЬНОЕ число')
                    err += 1
                else:
                    break

                err += 1
            # exit()
        if err < 3:
            sum = 0
            for i in range(n+1):
                if i % 3 == 0 or i % 5 == 0:
                    if i % 3 == 0 and i % 5 == 0:       # Ищем число кратные и 3 и 5
                        sum = sum + i*2
                    else:
                        sum = sum + i
            print(f'\nСумма чисел кратных 3 и 5 равна {sum}')

        else:
            print ('\nОшибка ввода данных')
        ask = input('\nХотите повторить? (y/n): ')
    else:
        exit()





