#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: huanglei

# 百鸡百钱

# 鸡翁钱五，所以最多只能买20只
# 鸡母钱三，所以最多只能买33只
# 鸡雏就是100-鸡翁-鸡母
# 我们用枚举法，把所有的可能性算一遍，效率低但是能算出结果
# i 定义为鸡翁，j定义为鸡母，k定义为鸡雏

for i in range(1, 21):
    for j in range(1, 34):
        k = 100 - i - j
        if (i*5 + j*3 + k/3) == 100 and k % 3 == 0:
            print('鸡翁: {} 鸡母: {} 鸡雏: {}'.format(i, j, k))
