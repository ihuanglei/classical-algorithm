#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: huanglei

# 闰年

for year in range(1700, 2022):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print('{} 是闰年'.format(year))
    else:
        print('{} 是平年'.format(year))
