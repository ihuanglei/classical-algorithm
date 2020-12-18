#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: huanglei

# 快速排序

# 快速排序的基本思想是

# 1. 从数列中挑出一个元素，称为 "基准"（pivot）
# 2. 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作
# 3. 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序

arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]

def quick_sort(arr, low, high):
    low1 = low
    high1 = high
    if low < high:
        pivot = arr[low]
        while low < high:

            while low < high and arr[high] > pivot:
                high = high - 1

            arr[low] = arr[high]

            while low < high and arr[low] <= pivot:
                low = low + 1

            arr[high] = arr[low]
            arr[low] = pivot

        quick_sort(arr, low1, low)
        quick_sort(arr, low + 1, high1)

quick_sort(arr, 0, len(arr) - 1)
print('排序后结果: {}'.format(arr))
