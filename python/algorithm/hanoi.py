#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: huanglei


# 算法:
# n为盘子个数

# n=1
# 直接把A上的一个盘子移动到C上，A --> C

# n=2
# 把小盘子从A放到B上，A --> B
# 把大盘子从A放到C上，A --> C
# 把小盘子从B放到C上，B --> C

# n=3
# 把A上的两个盘子，通过C移动到B上去，调用递归实现
# 把A上剩下的一个最大盘子移动到C上，A --> C
# 把B上两个盘子，借助于A,移到C上去，调用递归

# n=n
# 把A上的n-1个盘子，借助于C，移动到B上去，调用递归
# 把A上的最大盘子，也是唯一一个，移动到C上，A --> C
# 把B上n-1个盘子，借助于A，移动到C上，调用递归


def move(n, a, b, c):
    if n == 1:
        print('{} --> {}'.format(a, c))
    else:
        move(n-1, a, c, b)
        print('{} --> {}'.format(a, c))
        move(n-1, b, a, c)


move(3, 'A', 'B', 'C')
