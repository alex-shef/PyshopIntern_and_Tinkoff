"""
Во время разработки некоторой задачи Саша решил сгенерировать несколько новых тестов.
Каждый тест Саши должен представлять собой натуральное число, не меньшее l и не большее r.
Кроме того, натуральное число в тесте обязательно должно состоять из одинаковых цифр.
Например, число 999 подходит под это требование, а число 123 — нет.
Какое максимальное число различных тестов сможет создать Саша?

Формат входных данных
В единственной строке вводятся два натуральных числа l,r (1≤l,r≤10^18) — ограничения на тесты Саши.
Обратите внимания, что эти числа не вместятся в 32-битный тип данных,
используйте 64-битный при необходимости

Формат выходных данных
Выведите одно число — количество тестов, которое может сделать Саша.

Замечание
В первом тесте Саше подходят номера [4,5,6,7].
Во втором тесте подходят все числа, кратные 11, от 11 до 99.
"""

l, r = list(map(int, input().split()))
count = 0
for elem in range(l, r+1):
    if elem < 10 or elem % 11 == 0:
        count += 1
print(count)
