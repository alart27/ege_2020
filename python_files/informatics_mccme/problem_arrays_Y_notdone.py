"""
Известно, что на доске 8×8 можно расставить 8 ферзей так,
чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске,
определите, есть ли среди них пара бьющих друг друга.

Входные данные 
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты
8 ферзей.

Выходные данные 
Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.
"""


def solution(x, y):

    m = x[0]
    n = y[0]
    
    for i in range(1, 8):
        if x[i]
