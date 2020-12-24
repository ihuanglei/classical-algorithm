#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: huanglei

# 冒泡排序

arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]

for i in range(len(arr), 0, -1):
    for j in range(0, i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print('排序后结果: {}'.format(arr))
