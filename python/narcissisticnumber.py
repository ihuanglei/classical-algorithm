#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: huanglei

# 水仙花数

# 小技巧：
#
# 如果要取一个数的每一位数字，用当前数字除以单位取整然后再和10取余
# 举例说明:
# 数字:123
# 个位： int(123 / 1) % 10
# 十位： int(123 / 10) % 10
# 百位： int(123 / 100) % 10

for i in range(100, 1000):
    # 个位
    units = i % 10
    # 十位
    tens = int(i / 10) % 10
    # 百位
    hundreds = int(i / 100) % 10
    # 3次幂之和等于它本身，python中幂使用 **
    if (units ** 3 + tens ** 3 + hundreds ** 3) == i:
        print("{} 是水仙花数".format(i))
