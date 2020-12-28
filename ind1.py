#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ввести список А из 10 элементов, найти разность положительных элементов, и вывести ее
# на экран.

# import sys

if __name__ == '__main__':
    lst = [1, 3, -5, 3, 5, -8, 5, 34, -5, 15]
    r = len(lst)
    for i in range(0, r-1):
        if lst [i] >=0 and lst [i+1] >=0:
           print(lst[i] - lst[i + 1], end=' ')
