#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def cylinder(r, h):
    y_n = input("Нужна полная площадь цилиндра? да\нет: ").lower()

    if y_n == 'да':
        S_b = 2 * math.pi * r * h
        S = S_b + 2 * circle(r)
        print(S)

    else:
        print(2 * math.pi * r * h)


def circle(r):
    return math.pi * r ** 2


if __name__ == '__main__':
    r = int(input("r = "))
    h = int(input("h = "))
    cylinder(r, h)
