#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: huanglei

def fibonacci(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fibonacci(12)