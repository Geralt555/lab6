#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# В списке, состоящем из целых элементов, вычислить:
# произведение элементов списка, расположенных между первым и вторым нулевыми
# элементами.
# Преобразовать список таким образом, чтобы в первой его половине располагались элементы,
# стоявшие в нечетных позициях, а во второй половине - элементы, стоявшие в четных позициях.

# import sys

if __name__ == '__main__':
    a = list(map(int, input("Введите список: ").split()))
    if a.count(0) < 2:
        print('Не хватает нулевых элементов')
    x1 = x2 = -1
    for i in range(len(a)):
        if a[i] == 0:
            if x1 == -1:
                x1 = i
            elif x2 == -1:
                x2 = i
        if x1 != -1 and x2 != -1:
            break
    m = 1
    for i in range(x1 + 1, x2):
        m *= a[i]
    print("Произведение элементов списка, расположенных между первым и вторым"
          " нулевыми элементами равно:", m)
