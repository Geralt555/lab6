#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ввести список А из 10 элементов, найти разность положительных элементов, и вывести ее
# на экран.

# import sys

if __name__ == '__main__':
    lst = [1, 3, 5, 3, 5, 8, 5, 34, 5, 8, 9, 453, 36, 7, 4]
    r = len(lst) if len(lst) % 2 == 0 else len(lst) - 1
    for i in range(0, r, 2):
        print(lst[i] - lst[i + 1], end=' ')
