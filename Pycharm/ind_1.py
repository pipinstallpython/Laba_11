#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def test(number):
    if number > 0:
        positive()

    elif number < 0:
        negative()

    else:
        print("Ноль")


def positive():
    print("Положительное")


def negative():
    print("Отрицательное")


if __name__ == "__main__":
    test(int(input()))
