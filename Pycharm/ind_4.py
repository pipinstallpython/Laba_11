#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys


def get_input():
    return input()


def test_input(x):
    return x.isnumeric()


def str_to_int(x):
    return int(x)


def print_int(x):
    print(x)


if __name__ == '__main__':
    if test_input(x := get_input()):
        print_int(str_to_int(x))
    else:
        print("Введено не целое число", file=sys.stderr)
