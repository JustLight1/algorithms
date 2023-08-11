"""
D. Две фишки
Ограничение времени	4 секунды
Ограничение памяти	256Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Рита и Гоша играют в игру. У Риты есть n фишек, на каждой из которых написано
количество очков. Сначала Гоша называет число k, затем Рита должна выбрать две
фишки, сумма очков на которых равна заданному числу.

Рите надоело искать фишки самой, и она решила применить свои навыки
программирования для решения этой задачи. Помогите ей написать программу для
поиска нужных фишек.

Формат ввода
В первой строке записано количество фишек n, 2 ≤ n ≤ 104.

Во второй строке записано n целых чисел —– очки на фишках Риты в диапазоне
от -105 до 105.

В третьей строке —– загаданное Гошей целое число k, -105 ≤ k ≤ 105.

Формат вывода
Нужно вывести два числа —– очки на двух фишках, в сумме дающие k.

Если таких пар несколько, то можно вывести любую из них.

Если таких пар не существует, то вывести «None».

Пример 1
Ввод	            Вывод
6
-1 -1 -9 -7 3 -6
2
                    -1 3

Пример 2
Ввод	            Вывод
8
6 2 8 -3 1 1 6 10
100
                    None
"""


def two_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return numbers[i], numbers[j]
    return None, None


two_sum([-1, -1, -9, -7, 3, -6], 2)


# def twosum_with_sort(numbers, target):
#     numbers.sort()

#     left = 0
#     right = len(numbers) - 1
#     while left < right:
#         current_sum = numbers[left] + numbers[right]
#         if current_sum == target:
#             return numbers[left], numbers[right]
#         if current_sum < target:
#             left += 1
#         else:
#             right -= 1
#     return None, None

# def twosum_extra_ds(numbers, X):
#     previous = set()

#     for A in numbers:
#         Y = X - A
#         if Y in previous:
#             return A, Y
#         else:
#             previous.add(A)

#     return None, None
