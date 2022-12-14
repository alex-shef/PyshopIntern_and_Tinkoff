"""
У Артемия есть бесконечное число монет, каждая из которых одного из трех номиналов.
Его интересует, какие суммы от 1 до N рублей он может набрать в свой кошелек,
если там заранее лежала монета величиной в 1 рубль.

Формат входных данных
Первая строка содержит число N — ограничение на сумарную стоимость монет в кошельке (1≤N≤10^18).
Вторая строка содержит три числа A,B и C, задающие достоинства типов монет (1≤A,B,C≤100000).

Формат выходных данных
Выведите единственное число — количество сумм, которые можно набрать в кошельке.

Замечание
В первом примере возможны следующие варианты:
1=1
1+4=5
1+7=8
1+4+4=9
1+9=10
1+4+7=12
1+4+4+4=13
1+4+9=14
1+7+7=15
"""

n = int(input())
coins = list(map(int, input().split()))
sums = [1]
intermediate_sums = []
total_sums = [1]
while sums:
    for coin in coins:
        for sum_coins in sums:
            sum_coins += coin
            if sum_coins <= n and sum_coins not in total_sums:
                total_sums.append(sum_coins)
                intermediate_sums.append(sum_coins)
    sums = intermediate_sums.copy()
    intermediate_sums.clear()

print(len(total_sums))

