"""
Усложнение задачи фибоначчи.
Сделайте аналогичную функцию, но в которой
каждый следующий элемент - это сумма трёх предыдущих
Последовательность:
1, 1, 1, 3, 5, 9, 17...
"""


def fibo(n):
    fibo_list = [1, 1, 1]
    for i in range(n - 3):
        fibo_list.append(fibo_list[-3] + fibo_list[-2] + fibo_list[-1])
    return fibo_list[-1]


print(fibo(5))  # 5
print(fibo(80))  # 351892690889787253855
print(fibo(9))  # 57
