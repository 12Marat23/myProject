# import codewars_test as test

# =========================================================================================================================

# ==========================================================================================================================
# Simple string characters
# =========================================================================================================================
'''В этом ката вам будет предоставлена строка, и вашей задачей будет вернуть список целых чисел
 с подробным описанием количества прописных букв, строчных букв, цифр и специальных символов следующим образом.
 Solve("*'&ABCDabcde12345") = [4,5,5,3].
--the order is: uppercase letters, lowercase, numbers and special characters.
 '''
# import codewars_test as test


# def solve(s):
# uppercase = 0
# lowercase = 0
# numbers = 0
# special_characters = 0
#
# for i in s:
#     if i.isupper():
#         uppercase += 1
#     elif i.islower():
#         lowercase += 1
#     elif i.isdigit():
#         numbers += 1
#     else:
#         special_characters += 1
# return [uppercase, lowercase, numbers, special_characters]
'''Варианты решения:
 res = [0, 0, 0, 0]
    for c in s:
        i = 0 if c.isupper() else 1 if c.islower() else 2 if c.isdigit() else 3
        res[i] += 1
    return res
'''

#
# test.it("Basic tests")
# test.assert_equals(solve("Codewars@codewars123.com"), [1, 18, 3, 2])
# test.assert_equals(solve("bgA5<1d-tOwUZTS8yQ"), [7, 6, 3, 2])
# test.assert_equals(solve("P*K4%>mQUDaG$h=cx2?.Czt7!Zn16p@5H"), [9, 9, 6, 9])
# test.assert_equals(solve("RYT'>s&gO-.CM9AKeH?,5317tWGpS<*x2ukXZD"), [15, 8, 6, 9])
# test.assert_equals(solve("$Cnl)Sr<7bBW-&qLHI!mY41ODe"), [10, 7, 3, 6])
# test.assert_equals(solve("@mw>0=QD-iAx!rp9TaG?o&M%l$34L.nbft"), [7, 13, 4, 10])

# =========================================================================================================================

# ==========================================================================================================================
# Simple string characters
# =========================================================================================================================
# import codewars_test as test


'''Новое задание для вас!

Вы должны создать метод, который корректирует заданную временную строку.
Кроме того, возникла проблема, из-за которой многие временные цепочки были разорваны.
Время отформатировано с использованием 24-часовых часов, то есть с 00:00:00 до 23:59:59.'''

#
# def time_correct(t):
#     # your code here

#     def time_correct(t):
#         # your code here
#         if not t:
#             return t
#         try:
#             h, m, s = map(int, t.split(':'))
#             return '%02d:%02d:%02d' % ((h + (m + s // 60) // 60) % 24, (m + s // 60) % 60, s % 60)
#         except:
#             return None


# test.describe("Basic Tests")
# test.it("None or empty")
# test.assert_equals(time_correct(None), None)
# test.assert_equals(time_correct(""), "")
# test.it("Invalid Format")
# test.assert_equals(time_correct("001122"), None)
# test.assert_equals(time_correct("00;11;22"), None)
# test.assert_equals(time_correct("0a:1c:22"), None)
# test.assert_equals(time_correct("10:72:2"), None)
# test.it("Correction Tests")
# test.assert_equals(time_correct("09:10:01"), "09:10:01")
# test.assert_equals(time_correct("11:70:10"), "12:10:10")
# test.assert_equals(time_correct("19:99:99"), "20:40:39")
# test.assert_equals(time_correct("24:01:01"), "00:01:01")
# test.assert_equals(time_correct("52:01:01"), "04:01:01")

# =========================================================================================================================

# ==========================================================================================================================
# Ordered Count of Characters
# =========================================================================================================================

'''Подсчитайте количество вхождений каждого символа и верните его в виде (списка кортежей) в порядке появления. 
Для возврата пустого вывода (пустой список).

Обратитесь к настройке решения для точной реализации структуры данных в зависимости от вашего языка.'''
from collections import Counter

# def ordered_count(inp):
# word = []
# x = []
# inp = list(inp)
# for i in inp:
#     if i not in word:
#         word.append(i)
# for j in word:
#     x.append(inp.count(j))
# return list(zip(word, x))
'''Вариант решения:
return list(Counter(inp).items())
'''

# ordered_count('abracadabra')
# test.describe("Basic Tests")
#
# tests = (
#     ('abracadabra', [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]),
#     ('Code Wars', [('C', 1), ('o', 1), ('d', 1), ('e', 1), (' ', 1), ('W', 1), ('a', 1), ('r', 1), ('s', 1)])
# )
#
# for t in tests:
#     inp, exp = t
#     test.assert_equals(ordered_count(inp), exp)

# =========================================================================================================================

# ==========================================================================================================================
# Ordered Count of Characters
# =========================================================================================================================

'''На этой неделе возникла проблема с его поставками, и все овощи перепутались. 
На его кухне есть два важных аспекта приготовления пищи: все должно быть сделано гармонично, 
и ничто не может быть потрачено впустую. Поскольку монахи ведут учет, первым делом они сортируют смешанные овощи, 
а затем пересчитывают их, чтобы убедиться, что их достаточно, чтобы накормить всех студентов и жителей деревни.

Вам будет выдана строка со следующими овощами:

Возвращает список кортежей с количеством каждого овоща в порядке убывания. 
Если в смеси есть какие-либо другие овощи, выбросьте их. 
Если количество двух овощей одинаковое, отсортируйте их в обратном алфавитном порядке (Z->A).
'''

# def count_vegetables(string):
#     items = string.split()
#     veggies = ['cabbage', 'carrot', 'celery', 'cucumber', 'mushroom', 'onion', 'pepper', 'potato', 'tofu', 'turnip']
#     return sorted([(items.count(v), v) for v in veggies], reverse=True)


# @test.describe("Tests...")
# def _():
#     @test.it("Basic tests")
#     def _():
#         lst1 = [(2, 'tofu'),
#                 (2, 'potato'),
#                 (2, 'cucumber'),
#                 (2, 'cabbage'),
#                 (1, 'turnip'),
#                 (1, 'pepper'),
#                 (1, 'onion'),
#                 (1, 'mushroom'),
#                 (1, 'celery'),
#                 (1, 'carrot')]
#         s1 = 'potato tofu cucumber cabbage turnip pepper onion carrot celery mushroom potato tofu cucumber cabbage'
#         test.assert_equals(count_vegetables(s1), (lst1))
#         lst2 = [(15, 'turnip'),
#                 (15, 'mushroom'),
#                 (13, 'cabbage'),
#                 (10, 'carrot'),
#                 (9, 'potato'),
#                 (7, 'onion'),
#                 (6, 'tofu'),
#                 (6, 'pepper'),
#                 (5, 'cucumber'),
#                 (4, 'celery')]
#         s2 = (
#             'mushroom chopsticks chopsticks turnip mushroom carrot mushroom cabbage mushroom carrot tofu pepper cabbage potato cucumber '
#             'mushroom mushroom mushroom potato turnip chopsticks cabbage celery celery turnip pepper chopsticks potato potato onion cabbage cucumber '
#             'onion pepper onion cabbage potato tofu carrot cabbage cabbage turnip mushroom cabbage cabbage cucumber cabbage chopsticks turnip pepper '
#             'onion pepper onion mushroom turnip carrot carrot tofu onion tofu chopsticks chopsticks chopsticks mushroom cucumber chopsticks carrot '
#             'potato cabbage cabbage carrot mushroom chopsticks mushroom celery turnip onion carrot turnip cucumber carrot potato mushroom turnip  '
#             'mushroom cabbage tofu turnip turnip turnip mushroom tofu potato pepper turnip potato turnip celery carrot turnip')
#         test.assert_equals(count_vegetables(s2), (lst2))

# =========================================================================================================================

# ==========================================================================================================================
# Divide and Conquer
# =========================================================================================================================


'''Учитывая смешанный массив числовых и строковых представлений целых чисел, 
сложите нестроковые целые числа и вычтите общее количество строковых целых чисел.

Возвращает в виде числа.'''

# def div_con(x):
# your code here
# str_num = 0
# int_num = 0
# for i in x:
#     if type(i) == str:
#         str_num += int(i)
#     elif type(i) == int:
#         int_num += i
# return int_num-str_num

'''Варианты решения:
 return sum(n if isinstance(n, int) else -int(n) for n in x)
'''

# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(div_con([9, 3, '7', '3']), 2)
#         test.assert_equals(div_con(['5', '0', 9, 3, 2, 1, '9', 6, 7]), 14)
#         test.assert_equals(div_con(['3', 6, 6, 0, '5', 8, 5, '6', 2,'0']), 13)
#         test.assert_equals(div_con(['1', '5', '8', 8, 9, 9, 2, '3']), 11)
#         test.assert_equals(div_con([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7]), 61)

# =========================================================================================================================

# ==========================================================================================================================
# Between Extremes
# =========================================================================================================================

'''Учитывая массив чисел, верните разницу между наибольшим и наименьшим значениями.
Например:
[23, 3, 19, 21, 16] должно вернуться 20 (т.е. 23 - 3).
[1, 434, 555, 34, 112] должен возвращать 554 (т.е. 555 - 1).
Массив будет содержать минимум два элемента. Диапазон входных данных гарантирует, 
что значение max-min не вызовет переполнения целых чисел.'''

# def between_extremes(numbers):
#     return max(numbers)-min(numbers)


# @test.it("Basic tests")
# def basic_tests():
#     test.assert_equals(between_extremes([1, 1]), 0, 'Expecting zero when all numbers are equal')
#     test.assert_equals(between_extremes([-1, -1]), 0, 'Expecting zero when all numbers are equal')
#     test.assert_equals(between_extremes([1, -1]), 2)
#     test.assert_equals(between_extremes([21, 34, 54, 43, 26, 12]), 42)
#     test.assert_equals(between_extremes([-1, -41, -77, -100]), 99)


# =========================================================================================================================

# ==========================================================================================================================
# [Code Golf] How many times of getting closer until it is the same?
# =========================================================================================================================
'''В этом ката для гольфа вы получите 2 неотрицательных числа a и b, b равно или больше a.

Затем выполните следующую процедуру:

Добавьте a к b, затем разделите его на 2 целочисленным делением.

Повторяйте процедуру до тех пор, пока b не станет равным a.

Возвращает, сколько раз потребовалось, чтобы сделать b равным a.

Теперь в вашем коде ограничение по длине равно 35 в одной строке.

(Длина эталонного решения равна 31)'''

# def f(a, b): return len(bin(a-b))-3


# @test.describe("Sample Tests")
# def tests():
#     with open('/workspace/solution.txt', 'r') as file:
#         sol_code = file.read()
#
#         @test.it(f'Test for your code itself: Length is {len(sol_code)}')
#         def tests():
#             test.expect(len(sol_code) <= 35, f'{len(sol_code)} should be less or equal to 35.')
#             test.expect('\n' not in sol_code, 'Your code should be one line.')
#
#     @test.it('Basic Tests')
#     def tests():
#         test.assert_equals(f(0, 0), 0, 'Input a=0, b=0')
#         test.assert_equals(f(1, 2), 1, 'Input a=1, b=2')
#         test.assert_equals(f(3, 9), 3, 'Input a=3, b=9')
#         test.assert_equals(f(4, 20), 5, 'Input a=4, b=20')
#         test.assert_equals(f(5, 36), 5, 'Input a=5, b=36')

# =========================================================================================================================

# ==========================================================================================================================
# Fix My Phone Numbers
# =========================================================================================================================
'''О, слава богу, ты здесь! Последний стажер полностью все испортил!
Все телефонные номера наших клиентов были зашифрованы, 
и нам нужны эти телефонные номера, чтобы раздражать их бесконечными звонками по продажам!
Формат
Телефонные номера хранятся в виде строк и состоят из 11 цифр, например '02078834982', и всегда должны начинаться с 0.
Однако произошло нечто странное, и теперь все телефонные номера содержат множество случайных символов, 
пробелов, а некоторые вообще не являются телефонными номерами!
Задача
Учитывая строку, вы должны решить, содержит ли она действительный номер телефона или нет. 
Если это произойдет, верните исправленный номер телефона в виде строки, 
т.е. '02078834982' без пробелов или специальных символов, иначе верните "Не номер телефона".
'''

import re

# def is_it_a_num(s: str) -> str:
# reg = re.compile('[^0-9]')
# s = reg.sub('', s)
# if s != '' and len(s) == 11 and s[0] == '0':
#     return s
# else:
#     return "Not a phone number"

'''Варианты решения:
    t = ''.join(i for i in s if i.isdigit())
    return t if len(t) == 11 and t[0] == "0" else "Not a phone number"
    -----------------------
    return number if (len(number := "".join(c for c in s if c.isdigit())) == 11 and number[
        0] == "0") else "Not a phone number"
'''

# print(is_it_a_num("S:)0207ERGQREG88349F82!efRF)"))
# print(is_it_a_num("sjfniebienvr12312312312ehfWh"))
# print(is_it_a_num("stop calling me no I have never been in an accident"))
# print(is_it_a_num("v   uf  f 0tt2eg qe0b 8rtyq4eyq564()(((((165"))

# @test.describe("is_it_a_num")
# def test_group():
#     @test.it("Should pass sample tests")
#     def test_case():
#         test.assert_equals(is_it_a_num("S:)0207ERGQREG88349F82!efRF)"), "02078834982")
#         test.assert_equals(is_it_a_num("sjfniebienvr12312312312ehfWh"), "Not a phone number")
#         test.assert_equals(is_it_a_num("0192387415456"), "Not a phone number")
#         test.assert_equals(is_it_a_num("v   uf  f 0tt2eg qe0b 8rtyq4eyq564()(((((165"), "02084564165")
#         test.assert_equals(is_it_a_num("stop calling me no I have never been in an accident"), "Not a phone number")

# =========================================================================================================================

# ==========================================================================================================================
# Find the index of the second occurrence of a letter in a string
# =========================================================================================================================
'''В этом ката вам нужно написать функцию, которая принимает строку и букву в качестве входных данных, 
а затем возвращает индекс второго вхождения этой буквы в строку. 
Если в строке нет такой буквы, то функция должна возвращать значение -1. 
Если буква встречается в строке только один раз, то также следует вернуть значение -1.
Примеры:

second_symbol('Hello world!!!','l') --> 3
second_symbol('Hello world!!!', 'A') --> -1
'''

# def second_symbol(s, symbol):
# ind = (s.find(symbol) + 1)
# return s.find(symbol, ind)

'''Варианты решения:
return s.find(symbol, s.find(symbol)+1)
'''

# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it("Basic Test Cases")
#     def basic_test_cases():
#         test.assert_equals(second_symbol('Hello world!!!', 'l'), 3,
#                            'Find the index of the second symbol "l" in the string')
#         test.assert_equals(second_symbol('Hello world!!!', 'o'), 7,
#                            'Find the index of the second symbol "o" in the string')
#         test.assert_equals(second_symbol('Hello world!!!', 'A'), -1, 'The symbol "A" is not in the string')
#         test.assert_equals(second_symbol('', 'q'), -1, 'The symbol "q" is not in the string')
#         test.assert_equals(second_symbol('Hello', '!'), -1, 'The symbol "!" is not in the string')


# =========================================================================================================================

# ==========================================================================================================================
# Power of two
# =========================================================================================================================
'''Выполните функцию power_of_two/PowerOfTwo (или эквивалент, в зависимости от вашего языка), 
которая определяет, является ли данное неотрицательное целое число степенью двойки. 
Из соответствующей статьи в Википедии:

степень двойки - это число вида 2n, где n - целое число, 
т.е. результат возведения в степень с числом два в качестве основания и целым n в качестве показателя степени.

Вы можете предположить, что входные данные всегда действительны.'''

# def power_of_two(x):

'''Варианты решения:
    return bin(x).count('1') == 1
    return x and (not (x & (x - 1)))
    return x.bit_count() == 1
'''

# test.assert_equals(power_of_two(0), False)
# test.assert_equals(power_of_two(1), True)
# test.assert_equals(power_of_two(2), True)
# test.assert_equals(power_of_two(5), False)
# test.assert_equals(power_of_two(6), False)
# test.assert_equals(power_of_two(4096), True)

# =========================================================================================================================

# ==========================================================================================================================
# Dot Calculator
# =========================================================================================================================

'''Вы должны написать калькулятор, который принимает строки для ввода. 
Точки будут обозначать число в уравнении. 
С одной стороны будут точки, обозначающие оператора, и снова точки после оператора. Точки и оператор будут разделены одним пробелом.

Вот следующие допустимые операторы :
+ Addition
- Subtraction
* Multiplication
// Integer Division

Вам нужно будет вернуть строку, содержащую точки, столько, сколько возвращает уравнение. 
Если результат равен 0, верните пустую строку. 
Когда дело доходит до вычитания, первое число всегда будет больше или равно второму числу.
'''

# def calc(txt):
#     # This is the place to code!
#     a, op, b = txt.split()
#     a, b = len(a), len(b)
#     return '.' * eval(f'{a} {op} {b}')


# def tester(input, expected, optional_message=""):
#     test.assert_equals(input, expected, optional_message)
#
#
# @test.describe("Dot Calculator Sample Tests")
# def ExampleTests():
#     @test.it("Sample Tests")
#     def run_sample_tests():
#         tester(calc("..... + ..............."), "....................")
#         tester(calc("..... - ..."), "..")
#         tester(calc("..... - ."), "....")
#         tester(calc("..... * ..."), "...............")
#         tester(calc("..... * .."), "..........")
#         tester(calc("..... // .."), "..")
#         tester(calc("..... // ."), ".....")
#         tester(calc(". // .."), "")
#         tester(calc(". - ."), "")

# =========================================================================================================================

# ==========================================================================================================================
# Boxlines
# =========================================================================================================================

'''Дана коробка X * Y * Z, построенная путем упорядочивания 1*1*1 единичные блоки, 
напишите функцию f(X,Y,Z), которая возвращает количество ребер (следовательно, boxlines) 
длиной 1 (как внутри, так и снаружи блока).

Соседние блоки блоков имеют одинаковые края, поэтому 2*1*1 коробка будет иметь 20 ребер, а не 24
X, Y и Z строго положительны и могут достигать 2 ^ 16 - 1
'''

# def f(a, b, c):
#     #  Your code here
#     return 3 * (a * b * c) + 2 * (a * b + b * c + a * c) + a + b + c


# @test.describe("Tests")
# def tests():
#     # Use "it" to identify the conditions you are testing for
#     @test.it("Example test")
#     def example_test():
#         test.assert_equals(f(2, 1, 1), 20)
#         test.assert_equals(f(1, 2, 3), 46)
#         test.assert_equals(f(2, 2, 2), 54)

# =========================================================================================================================

# ==========================================================================================================================
# 99 Bottles of Beer
# =========================================================================================================================
'''Завершите функцию, которая возвращает текст песни "99 бутылок пива" в виде массива строк: 
каждая строка должна быть отдельным элементом - смотрите пример внизу.

Примечание: чтобы избежать жестко запрограммированных решений, размер вашего кода ограничен 1000 символами

Текст песни
99 бутылок пива на стене, 99 бутылок пива.
Возьмите одну и передайте по кругу, на стене 98 бутылок пива.

98 бутылок пива на стене, 98 бутылок пива.
Возьмите одну и передайте по кругу, на стене 97 бутылок пива.

...и так далее.
.
.
.
3 бутылки пива на стене, 3 бутылки пива.
Возьмите одну и передайте по кругу, 2 бутылки пива на стене.

2 бутылки пива на стене, 2 бутылки пива.
Возьмите одну и передайте по кругу, 1 бутылка пива на стене.

1 бутылка пива на стене, 1 бутылка пива.
Возьмите одну и передайте по кругу, больше никаких бутылок пива на стене.

Больше никаких бутылок пива на стене, больше никаких бутылок пива.
Сходи в магазин и купи еще, на стене 99 бутылок пива.
'''

# def sing():
#     # your code here
#
#     print(sing())
#
#
# @test.describe('Example Tests')
# def example_tests():
#     @test.it("It should work for sing test")
#     def _():
#         test.assert_equals(sing()[0], '99 bottles of beer on the wall, 99 bottles of beer.')
#         test.assert_equals(sing()[199], 'Go to the store and buy some more, 99 bottles of beer on the wall.')

# =========================================================================================================================

# ==========================================================================================================================
# 99 Bottles of Beer
# =========================================================================================================================

'''Ваша задача состоит в том, чтобы написать функцию, которая принимает три целых числа 
a, b и c в качестве аргументов и возвращает True, если ровно два из трех целых чисел являются положительными числами 
(больше нуля), и False - в противном случае.
Примеры:
two_are_positive(2, 4, -3) == Истинно
two_are_positive(-4, 6, 8) == Истинно
two_are_positive(4, -6, 9) == Истинно
two_are_positive(-4, 6, 0) == Ложно
two_are_positive(4, 6, 10) == Ложно
two_are_positive(-14, -3, -4) == Ложь
'''

# def two_are_positive(a, b, c):
#     return sum([a > 0, b > 0, c > 0]) == 2


# @test.it("Example Tests")
# def example_tests():
#     test.assert_equals(two_are_positive(2, 4, -3), True)
#     test.assert_equals(two_are_positive(-4, 6, 8), True)
#     test.assert_equals(two_are_positive(4, -6, 9), True)
#     test.assert_equals(two_are_positive(-4, 6, 0), False)
#     test.assert_equals(two_are_positive(4, 6, 10), False)
#     test.assert_equals(two_are_positive(-14, -3, -4), False)

# =========================================================================================================================

# ==========================================================================================================================
#  Training Time
# =========================================================================================================================

'''Создайте функцию shuffleIt. Функция принимает два или более параметра. 
Первый параметр arr - это массив чисел, за которым следует произвольное количество числовых массивов. 
Каждый числовой массив содержит два числа, которые являются индексами для элементов в arr 
(числа всегда будут находиться в пределах допустимых значений). 
Для каждого такого массива поменяйте местами элементы. 
Попробуйте использовать все свои новые навыки: 
функции стрелок, оператор распространения, деструктурирование и остальные параметры'''

# def shuffle_it(arr, *X):
#     for x, y in X:
#         arr[x], arr[y] = arr[y], arr[x]
#     return arr


# @test.describe("shuffle_it")
# def shuffle_it():
#     @test.it("Basic tests")
#     def basic_tests():
#         test.assert_equals(shuffle_it([1, 2, 3, 4, 5], [1, 2]), [1, 3, 2, 4, 5])
#         test.assert_equals(shuffle_it([1, 2, 3, 4, 5], [1, 2], [3, 4]), [1, 3, 2, 5, 4])
#         test.assert_equals(shuffle_it([1, 2, 3, 4, 5], [1, 2], [3, 4], [2, 3]), [1, 3, 5, 2, 4])
#         test.assert_equals(shuffle_it([1, 2, 3, 4, 5], [4, 4]), [1, 2, 3, 4, 5])
#         test.assert_equals(shuffle_it([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

# =========================================================================================================================

# ==========================================================================================================================
#  Tram Capacity
# =========================================================================================================================

'''В Линейном королевстве есть ровно одна трамвайная линия. 
Он имеет n остановок, пронумерованных от 1 до n в порядке движения трамвая. 
На i-й остановке пассажиры ai выходят из трамвая, в то время как пассажиры bi входят в него. 
Трамвай пустеет еще до того, как прибывает на первую остановку.

Ваша задача
Рассчитайте минимальную вместимость трамвая таким образом, 
чтобы количество людей внутри трамвая никогда не превышало эту вместимость. 
Обратите внимание, что на каждой остановке все выходящие пассажиры выходят до того, 
как любой входящий пассажир войдет в трамвай.

Объяснение:

Количество пассажиров в трамвае перед прибытием равно 0.
На первой остановке в трамвай заходят 3 пассажира, и количество пассажиров внутри трамвая становится равным 3.
На второй остановке 2 пассажира выходят из трамвая (1 пассажир остается внутри). 
Затем в трамвай заходят 5 пассажиров. Сейчас в трамвае находятся 6 пассажиров.
На третьей остановке из трамвая выходят 4 пассажира (2 пассажира остаются внутри). 
Затем в трамвай заходят 2 пассажира. Сейчас в трамвае находятся 4 пассажира.
Наконец, все оставшиеся пассажиры внутри трамвая выходят из него на конечной остановке. 
Сейчас в трамвае нет пассажиров, что соответствует ограничениям.

Поскольку количество пассажиров в трамвае никогда не превышает 6, 
вместимости в 6 человек вполне достаточно. Кроме того, трамвай не может иметь вместимость менее 6 человек. 
Следовательно, правильный ответ - 6.
'''

# def tram(stops, descending, onboarding):
# passenger = 0
# passenger_Max = 0
# for i in range(0, stops):
#     passenger -= descending[i]
#     passenger += onboarding[i]
#     passenger_Max = max(passenger, passenger_Max)
# return passenger_Max
'''Варианты решения:
return max(sum(onboarding[:i]) - sum(descending[:i]) for i in range(stops + 1))
'''

# @test.describe("Tram capacity")
# def tram_capacity():
#     @test.it("Example tests")
#     def example_tests():
#         test.assert_equals(tram(4, [0, 2, 4, 4], [3, 5, 2, 0]), 6)
#         test.assert_equals(tram(2, [0, 2, 4, 4], [3, 5, 2, 0]), 6)
#         test.assert_equals(tram(1, [0, 2, 4, 4], [3, 5, 2, 0]), 3)
#         test.assert_equals(tram(10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]), 25)
#         test.assert_equals(tram(5, [0, 2, 4, 14, 2], [3, 5, 14, 0, 0]), 16)

# =========================================================================================================================

# ==========================================================================================================================
#  Power of 4
# =========================================================================================================================

'''Напишите метод, который возвращает значение true, если данный параметр имеет степень 4, 
и значение false, если это не так. Если параметр не является целым числом (например, строкой, массивом), 
метод также должен возвращать значение false.

(В C# Integer означает все целочисленные типы, такие как Int16, Int32,.....)

isPowerOf4 1024 #should return True
isPowerOf4  102 #should return False
isPowerOf4   64 #should return True
'''
from math import log, floor

# def powerof4(n):
# if type(n) in (float, int) and n > 0:
#     return log(n, 4).is_integer()
# return False


# @test.describe('Example Tests')
# def example_tests():
#     test.assert_equals(powerof4(4), True, "Wrong result for 4")
#     test.assert_equals(powerof4(40), False, "Wrong result for 40")
#     test.assert_equals(powerof4(1), True, "Wrong result for 1")

# =========================================================================================================================

# ==========================================================================================================================
#  "Center yourself", says the monk.
# =========================================================================================================================

'''Ваша компания MRE Tech наняла духовного консультанта, 
который посоветовал новую политику баланса: не принимайте чью-либо сторону, не отдавайте предпочтение, 
оставайтесь посередине. Эта политика применима даже к программному обеспечению, 
в котором все строки теперь должны располагаться по центру. Вы - жалкая душа, чтобы воплотить это в жизнь.

Задача
Реализуйте функцию center, которая принимает строку strng, 
целочисленную ширину и необязательную символьную заливку (по умолчанию: ' ') и 
возвращает новую строку длины и ширины, где strng находится по центру, а справа и слева заполнено заливкой.

center(strng, width, fill=' ')

If the left and right padding cannot be of equal length make the padding on the left side one character longer.

If strng is longer than width return strng unchanged.

Examples
center('a', 3)  # returns " a "
center('abc', 10, '_')  # returns "____abc___"
center('abcdefg', 2)  # returns "abcdefg"
'''

# def center(strng, width, fill=' '):
#     d = max(width - len(strng), 0)
#     return fill * ((d + 1) // 2) + strng + fill * (d // 2)


# print(center("a", 3))
# print(center("abc", 10, '_'))
# print(center("abcdefg", 2))
#
# @test.describe("tests suite")
# def tests_suite():
#     @test.it("sample tests")
#     def sample_tests():
#         test.assert_equals(center("a", 3), " a ")
#         test.assert_equals(center("abc", 10, '_'), "____abc___")
#         test.assert_equals(center("abcdefg", 2), "abcdefg")

# =========================================================================================================================

# ==========================================================================================================================
#  Page replacement algorithms: FIFO
# =========================================================================================================================

'''Ваша задача - реализовать этот алгоритм. Функция примет в качестве входных данных два параметра: 
максимальное количество страниц, которые могут храниться в памяти одновременно n, и список ссылок, содержащий цифры.
Каждое число представляет собой запрос страницы для определенной страницы 
(вы можете видеть это число как уникальный идентификатор страницы). 
Ожидаемый результат - это состояние памяти после применения алгоритма. 
Обратите внимание, что когда страница вставляется в память, она остается в том же положении до тех пор, 
пока не будет удалена из памяти из-за ошибки страницы.

Пример:
Дано:

N = 3,
СПИСОК ЛИТЕРАТУРЫ = [1, 2, 3, 4, 2, 5],
* 1 прочитано, ошибка страницы --> память = [1];
* прочитано 2, ошибка страницы --> память = [1, 2];
* прочитано 3, ошибка страницы --> память = [1, 2, 3];
* прочитано 4, ошибка страницы --> память = [4, 2, 3];
* 2 считано, уже в памяти, ничего не происходит;
* прочитано 5, ошибка страницы --> память = [4, 5, 3].
Итак, в конце у нас есть список [4, 5, 3], который вы должны вернуть. 
Если не все ячейки в памяти будут заняты после применения алгоритма, заполните оставшиеся ячейки 
(в конце списка) значением -1, чтобы обозначить пустоту 
(обратите внимание, что идентификаторы всегда будут >= 1).'''

# def fifo(n, reference_list):
#     memory = [-1] * n
#     c = 0
#
#     for ref in reference_list:
#         if ref in memory:
#             continue
#
#         memory[c] = ref
#         c = (c + 1) % n
#
#     return memory


# @test.describe("Basic Tests")
# def basic_tests():
#     @test.it("Basic Tests")
#     def basic_tests():
#         tests = [
#             [3, [1, 2, 3, 4, 2, 5], [4, 5, 3]],
#             [5, [], [-1, -1, -1, -1, -1]],
#             [4, [1, 2, 3, 3, 4, 5, 1], [5, 1, 3, 4]],
#             [4, [1, 1, 1, 2, 2, 3], [1, 2, 3, -1]],
#             [1, [5, 4, 3, 3, 4, 10], [10]],
#             [3, [1, 1, 1, 1, 1, 1, 1, 1], [1, -1, -1]],
#             [5, [10, 9, 8, 7, 7, 8, 7, 6, 5, 4, 3, 4, 3, 4, 5, 6, 5], [5, 4, 3, 7, 6]]
#         ]
#
#         for t in tests:
#             test.assert_equals(fifo(t[0], t[1][:]), t[2], f"N = {t[0]}, REFERENCE LIST = {t[1]}")

# =========================================================================================================================

# ==========================================================================================================================
#  Help Suzuki rake his garden!
# =========================================================================================================================
'''В монастыре есть великолепный дзенский сад, выложенный из белого гравия и камней, 
и монахи каждый день старательно разгребают его граблями. 
Обладающий острым зрением Сузуки всегда высматривает все, что заползает в сад и что необходимо 
удалять во время ежедневной уборки граблями, например насекомых или мох.

Вам будет предоставлена строка, представляющая сад, например:

сад = 'гравий гравий гравий гравий гравий гравий гравий гравий гравий гравий гравий рок пуля 
муравей улитка рок гравий гравий гравий гравий гравий гравий гравий гравий гравий гравий гравий гравий 
рок муравей слаг слаг гравий гравий гравий гравий гравий гравий гравий гравий улитка породы улитка 
слизень гравий гравий гравий гравий гравий гравий гравий гравий гравий паук гравий, мох, гравий гравий 
гравий гравий гравий гравий гравий гравий улитка, муравей мох, гравий гравий гравий гравий гравий гравий 
гравий гравий гравий улитка слизень рок гравий гравий гравий гравий гравий гравий гравий гравий рок, улитки, 
рок гравий гравий гравий гравий гравий гравий гравий гравий рок паук'
Выгребите все предметы, которые не являются камнем или гравием, и замените их гравием таким образом, чтобы:

сад = 'слизняк-паук, каменный гравий, гравийный гравий, гравийный гравий, гравийный гравий, гравийный гравий'
Возвращает строку, в которой все элементы, кроме камня или гравия, заменены на gravel:

сад = 'гравий гравий гравий гравий гравий гравий гравий гравий гравий рок'''

# def rake_garden(garden):


# return " ".join(w if w == "rock" else "gravel" for w in garden.split())
'''Варианты решения:
1)
VALID = {'gravel', 'rock'}
def rake_garden(garden):
    return ' '.join(a if a in VALID else 'gravel' for a in garden.split())
2)
    return ' '.join(word if word in ('rock', 'gravel') else 'gravel' for word in garden.split())
'''

# garden1 = 'slug spider rock gravel gravel gravel gravel gravel gravel gravel'
#
# print(rake_garden(garden1))

# @test.describe("Tests...")
# def _():
# @test.it("Fixed tests")
# def _():
#     garden1 = 'slug spider rock gravel gravel gravel gravel gravel gravel gravel'
#     test.assert_equals(rake_garden(garden1), 'gravel gravel rock gravel gravel gravel gravel gravel gravel gravel')
#
#     garden2 = 'gravel gravel gravel gravel gravel gravel gravel gravel gravel rock slug ant gravel ' \
#               'gravel snail rock gravel gravel gravel gravel gravel gravel gravel slug gravel ant gravel ' \
#               'gravel gravel gravel rock slug gravel gravel gravel gravel gravel snail gravel gravel rock ' \
#               'gravel snail slug gravel gravel spider gravel gravel gravel gravel gravel gravel gravel ' \
#               'gravel moss gravel gravel gravel snail gravel gravel gravel ant gravel gravel moss gravel ' \
#               'gravel gravel gravel snail gravel gravel gravel gravel slug gravel rock gravel gravel rock ' \
#               'gravel gravel gravel gravel snail gravel gravel rock gravel gravel gravel gravel gravel ' \
#               'spider gravel rock gravel gravel'
#     test.assert_equals(rake_garden(garden2),
#                        'gravel gravel gravel gravel gravel gravel gravel gravel gravel rock '
#                        'gravel gravel gravel gravel gravel rock gravel gravel gravel gravel '
#                        'gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel '
#                        'rock gravel gravel gravel gravel gravel gravel gravel gravel gravel rock '
#                        'gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel '
#                        'gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel '
#                        'gravel gravel gravel gravel gravel gravel gravel gravel gravel gravel '
#                        'gravel gravel gravel gravel gravel gravel gravel rock gravel gravel '
#                        'rock gravel gravel gravel gravel gravel gravel gravel rock gravel gravel '
#                        'gravel gravel gravel gravel gravel rock gravel gravel')

# =========================================================================================================================

# ==========================================================================================================================
#  Traffic Count During Peak Hours
# =========================================================================================================================
'''Вы работаете в компании, которая анализирует количество трафика на определенном перекрестке
в часы пик с 16:00 до 20:00. Каждый день вам выдается список, содержащий количество транспортных средств, 
которые проезжают через перекресток каждые 10 минут с 16:00 до 20:00 вечера.

Ожидается, что вы вернете список кортежей, 
каждый из которых содержит час и максимальный объем трафика за каждый час.

Например:
a1 = [23,24,34,45,43,23,57,34,65,12,19,45, 54,65,54,43,89,48,42,55,22,69,23,93]

traffic_count(a1) ==> [('4:00pm', 45), ('5:00pm', 65), ('6:00pm', 89), ('7:00pm', 93)]
All values in the given list are integers.

Все значения в данном списке являются целыми числами.
'''

# def traffic_count(array):

# t = []
# for i in range(4, 8):
#     x = array[0:6]
#     del array[0:6]
#     t.append((f'{i}:00pm', max(x)))
# return t


'''Варианты решения:
1) return [('4:00pm', max(array[:6])), ('5:00pm', max(array[6:12])), ('6:00pm', max(array[12:18])),
            ('7:00pm', max(array[18:]))]
2) return [('{}:00pm'.format(i + 4), max(array[i * 6:(i + 1) * 6])) for i in range(4)]
'''

# @test.describe("traffic_count")
# def traffic_count():
#     @test.it("Example tests")
#     def example_tests():
#         a1 = [23, 24, 34, 45, 43, 23, 57, 34, 65, 12, 19, 45, 54, 65, 54, 43, 89, 48, 42, 55, 22, 69, 23, 93]
#         r1 = [('4:00pm', 45), ('5:00pm', 65), ('6:00pm', 89), ('7:00pm', 93)]
#         test.assert_equals(traffic_count(a1), r1)
#
#         a2 = [22, 31, 70, 22, 49, 62, 38, 26, 44, 43, 67, 30, 76, 77, 18, 47, 42, 57, 30, 38, 87, 94, 7, 18]
#         r2 = [('4:00pm', 70), ('5:00pm', 67), ('6:00pm', 77), ('7:00pm', 94)]
#         test.assert_equals(traffic_count(a2), r2)

# =========================================================================================================================

# ==========================================================================================================================
#  Battle of the characters (Easy)
# =========================================================================================================================

'''Описание:
Группы персонажей решили устроить битву. Помогите им выяснить, какая группа более могущественна. 
Создайте функцию, которая будет принимать 2 строки и возвращать ту, которая сильнее.

Правила:
Каждый персонаж обладает своей собственной силой: A = 1, B = 2, ... Y = 25, Z = 26
Строки будут состоять только из заглавных букв
Только две группы вступили в бой.
Выигрывает группа, чья суммарная мощность (A + B + C + ...) больше.
Если силы равны, то это ничья.
Примеры:
      * "ОДИН", "ДВА" -> "ДВА"`
      * "ОДИН", "НЕО" -> "Ничья!"
A = 65, Z = 90
'''

# def battle(x, y):


# Let the battle begin!
# if sum(map(lambda num: ord(num)-64, x)) == sum(map(lambda num: ord(num)-64, y)):
#     return "Tie!"
# elif sum(map(lambda num: ord(num)-64, x)) > sum(map(lambda num: ord(num)-64, y)):
#     return x
# return y
'''Вариани решения:
an = lambda word: sum(ord(i) - 64 for i in word)
    return x if an(x) > an(y) else y if an(y) > an(x) else 'Tie!'
'''

# @test.describe("Tests")
# def tests():
#     @test.it("Basic tests")
#     def basic_tests():
#         test.assert_equals(battle("AAA", "Z"), "Z", "Unfair fight!")
#         test.assert_equals(battle("ONE", "TWO"), "TWO", "Unfair fight!")
#         test.assert_equals(battle("ONE", "NEO"), "Tie!", "Unfair fight!")
#         test.assert_equals(battle("FOUR", "FIVE"), "FOUR", "Unfair fight!")

# =========================================================================================================================

# ==========================================================================================================================
# Find the capitals
# =========================================================================================================================

'''Напишите функцию, которая принимает в качестве аргумента одну строку (слово). 
Функция должна возвращать упорядоченный список, содержащий индексы всех заглавных букв в строке.

Пример
Test.assertSimilar( заглавные буквы('CodEWaRs'), [0,3,4,6] );
'''

# def capitals(word):
# your code here
# return [i for i in range(len(word)) if word[i].isupper()]
'''Варианты решения:
return [i for (i, c) in enumerate(word) if c.isupper()]
'''

# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(capitals('CodEWaRs'), [0, 3, 4, 6])

# =========================================================================================================================

# ==========================================================================================================================
# Find the divisors!
# =========================================================================================================================

'''создайте функцию с именем divisors/Делители, которая принимает целое число n > 1 
и возвращает массив со всеми делителями целого числа (за исключением 1 и самого числа), 
от наименьшего до наибольшего. Если число простое, верните строку
 '(integer) is prime' (null в C#, пустая таблица в COBOL) 
 (используйте либо строку a в Haskell, либо результат<Vec<u32>, String> в Rust).

Пример:
делители(12); #должно возвращать [2,3,4,6]
делители(25); #должно возвращать [5]
делители(13); #должно возвращать "13 - простое число"'''

# def divisors(integer):
#     c = []
#     for i in range(2, integer):
#         if integer % i == 0:
#             c.append(i)
#     if len(c) == 0:
#         c = f"{integer} is prime"
#     return c

'''Варианты решения:
  l = [a for a in range(2, integer) if integer % a == 0]
    if len(l) == 0:
        return str(integer) + " is prime"
    return l

'''

# @test.describe("Fixed Tests")
# def basic_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(divisors(15), [3, 5])
#         test.assert_equals(divisors(253), [11, 23])
#         test.assert_equals(divisors(24), [2, 3, 4, 6, 8, 12])
#         test.assert_equals(divisors(25), [5])
#         test.assert_equals(divisors(13), "13 is prime")
#         test.assert_equals(divisors(3), "3 is prime")
#         test.assert_equals(divisors(29), "29 is prime")

# =========================================================================================================================

# ==========================================================================================================================
# Find the divisors!
# =========================================================================================================================
'''Ваша задача состоит в том, чтобы написать функцию, которая принимает число в качестве аргумента и 
возвращает некоторое число. Но в чем проблема? Вам нужно угадать, какое число должно быть возвращено. 
Смотрите пример тестового примера. Удачи. Подсказка: Вам следует быть немного осторожнее при подсчете...'''

# def secret_number(n):
#     return bin(n).count(str(n % 2)) ** 2


# print(secret_number(10))
# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it("Example Tests")
#     def example_tests():
#         test.assert_equals(secret_number(2), 4)
#         test.assert_equals(secret_number(5), 4)
#         test.assert_equals(secret_number(10), 9)
#         test.assert_equals(secret_number(15), 16)
#         test.assert_equals(secret_number(31), 25)
#         test.assert_equals(secret_number(9978), 36)
#         test.assert_equals(secret_number(1234567), 121)
#         test.assert_equals(secret_number(14556237892), 400)

# =========================================================================================================================

# ==========================================================================================================================
# Fizz / Buzz
# =========================================================================================================================
'''Напишите функцию, которая принимает целое число и возвращает массив [A, B, C], 
где A - число, кратное 3 (но не 5) ниже заданного целого, 
B - число, кратное 5 (но не 3) ниже заданного целого, 
а C - число кратных 3 и 5 ниже заданного целого числа.

Например, решение(20) должно возвращать [5, 2, 1]'''

# import codewars_test as test


# def solution(number):
#     A = (number - 1) // 3
#     B = (number - 1) // 5
#     C = (number - 1) // 15
#     return [A - C, B - C, C]


# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(solution(20), [5, 2, 1])
#         test.assert_equals(solution(2), [0, 0, 0])
#         test.assert_equals(solution(14), [4, 2, 0])
#         test.assert_equals(solution(30), [8, 4, 1])
#         test.assert_equals(solution(141), [37, 19, 9])

# =========================================================================================================================

# ==========================================================================================================================
# Fizz / Buzz
# =========================================================================================================================

'''Массив размером N x M представляет собой пиксели изображения. 
Каждая ячейка этого массива содержит массив размером 3 с информацией о цвете пикселя: [R,G,B]

Преобразуйте цветное изображение в среднее изображение в оттенках серого.
Массив [R,G,B] содержит целые числа от 0 до 255 для каждого цвета.
Чтобы преобразовать цветной пиксель в пиксель в оттенках серого, усредните значения этого пикселя:

p = [R,G,B] => [(R+G+B)/3, (R+G+B)/3, (R+G+B)/3]
Примечание: значения для пикселя должны быть целыми числами, поэтому вы должны округлить значения с плавающей 
точкой до ближайшего целого числа.

Пример
Вот пример изображения размером 2х2:

[
 [ [123, 231, 12], [56, 43, 124] ],
 [ [78, 152, 76], [64, 132, 200] ]
]

Вот ожидаемое изображение после преобразования:
[
 [ [122, 122, 122], [74, 74, 74] ],
 [ [102, 102, 102], [132, 132, 132] ]
]
'''


def color_2_grey(image):
    return [[[int(round(sum(rgb) / 3))] * 3 for rgb in row] for row in image]



print(color_2_grey(
    [[[123, 231, 12], [56, 43, 124]], [[78, 152, 76], [64, 132, 200]]],
))

import codewars_test as test
from copy import deepcopy

# @test.describe("Sample Tests")
# def sample_tests():
#     def run_test(input_, expected):
#         actual = color_2_grey(deepcopy(input_))
#         test.expect(isinstance(actual, list), f'Output should be a 3D list: expected {actual} to be a list',
#                     allow_raise=True)
#         test.assert_equals(len(actual), len(expected), f'Output should have the same dimensions as the input',
#                            allow_raise=True)
#         for r in range(len(input_)):
#             test.expect(isinstance(actual[r], list), f'Output should be a 3D list: expected {actual[r]} to be a list',
#                         allow_raise=True)
#             test.assert_equals(len(actual), len(expected), f'Output should have the same dimensions as the input',
#                                allow_raise=True)
#             for c in range(len(input_[r])):
#                 test.expect(isinstance(actual[r][c], list),
#                             f'Output should be a 3D list: expected {actual[r][c]} to be a list', allow_raise=True)
#                 test.assert_equals(actual[r][c], expected[r][c], f'Input pixel: {input_[r][c]}\nOutput pixel',
#                                    allow_raise=False)
#
#     @test.it("Basic Tests")
#     def basic_tests():
#         tests = [
#             (
#                 [[[123, 231, 12], [56, 43, 124]], [[78, 152, 76], [64, 132, 200]]],
#                 [[[122, 122, 122], [74, 74, 74]], [[102, 102, 102], [132, 132, 132]]],
#             ),
#             (
#                 [[[88, 110, 23]], [[93, 53, 35]], [[59, 65, 5]], [[184, 194, 2]]],
#                 [[[74, 74, 74]], [[60, 60, 60]], [[43, 43, 43]], [[127, 127, 127]]],
#             ),
#         ]
#
#         for input_, expected in tests:
#             run_test(input_, expected)
