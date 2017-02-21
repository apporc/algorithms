#!/usr/bin/env python
import sys


def recursive_pow(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    if n % 2 == 0:
        return recursive_pow(x, n / 2) ** 2
    else:
        return x * recursive_pow(x, (n - 1) / 2) ** 2


def lgn_pow(x, n):
    if n >= 0:
        return recursive_pow(x, n)
    else:
        return 1.0 / recursive_pow(x, -n)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: ./lgn_pow.py x n')
    else:
        print('Input: %s' % sys.argv)
        result = lgn_pow(int(sys.argv[1]), int(sys.argv[2]))
        print('Result: %s' % result)
