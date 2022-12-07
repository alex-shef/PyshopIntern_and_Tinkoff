"""
У Кости есть бумажка, на которой написано n чисел.
Также у него есть возможность не больше, чем k раз, взять любое число с бумажки,
после чего закрасить одну из старых цифр, а на ее месте написать новую произвольную цифру.
На какое максимальное значение Костя сможет увеличить сумму всех чисел на листочке?

Формат входных данных
В первой строке входного файла даны два целых числа n,k — количество чисел на бумажке и ограничение на число операций.
(1≤n≤1000,1≤k≤10^4).
Во второй строке записано n чисел a_i — числа на бумажке (1≤a_i≤10^9)

Формат выходных данных
В выходной файл выведите одно число — максимальную разность между конечной и начальной суммой.

Замечание
В первом примере Костя может изменить две единицы на две девятки,
в результате чего сумма чисел увеличится на 16.
Во втором примере Костя меняет число 85 на 95.
В третьем примере можно ничего не менять.
Обратите внимание, что ответ может превышать вместимость 32-битного типа данных.
"""

# numbers = ['99', '1', '85']
# n, k = 3, 1

n, k = list(map(int, input().split()))
numbers = list(map(int, input().split()))

sum1 = sum(numbers)
print('sum1', sum1)
sorted_numbers = list(map(str, sorted(numbers, reverse=True)))
sorted_numbers_with_whitespace = []
for elem in sorted_numbers:
    if len(elem) != len(sorted_numbers[0]):
        elem = ' '*(len(sorted_numbers[0])-len(elem)) + elem
    sorted_numbers_with_whitespace.append(elem)

sorted_numbers_with_whitespace_after_replace = sorted_numbers_with_whitespace
for number_position in range(len(sorted_numbers[0])):
    number_positions_list = [digit[number_position] for digit in sorted_numbers_with_whitespace]
    number_positions_dict = {num: digit for num, digit in enumerate(number_positions_list)}
    print(number_positions_dict)
    for number in range(n):
        index_min = next(key for key, value in number_positions_dict.items()
                         if value == min(number_positions_dict.values()))
        value_min = number_positions_dict.pop(index_min)
        if value_min not in ('9', ' '):
            elem = sorted_numbers_with_whitespace[index_min].replace(value_min, '9', 1)
            k -= 1
        else:
            elem = sorted_numbers_with_whitespace[index_min]
        sorted_numbers_with_whitespace_after_replace[index_min] = elem
        if k == 0:
            break
    if k == 0:
        break
    sorted_numbers_with_whitespace = sorted_numbers_with_whitespace_after_replace
print(sorted_numbers_with_whitespace_after_replace)
sum2 = sum(map(int, sorted_numbers_with_whitespace_after_replace))
print('sum2', sum2)
print('max difference:', sum2-sum1)
