#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def counter():
    n = 1
    while True:
        x = int(input("Введите число: "))
        if x == 0:
            return print(f"Произведение равно: {n}")
        else:
            n *= x
            print(f"Произведение равно: {n}")


if __name__ == '__main__':
    counter()
