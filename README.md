# classical-algorithm 经典算法

## 九九乘法表

九九乘法表是中国古代筹算中进行乘法、除法、开方等运算的基本计算规则，沿用至今已有两千多年。在《荀子》、《管子》、《淮南子》、《战国策》等书中就能找到“三九二十七”、“六八四十八”、“四八三十二”、“六六三十六”等句子。

代码：
```python
for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}'.format(j, i, j*i), end=' ')
    print()
```
示例: [点我查看python代码](python/algorithm/99mult.py "九九乘法表")

***

## 闰年

闰年是公历中的名词。闰年分为普通闰年和世纪闰年。

普通闰年：公历年份是4的倍数的，且不是100的倍数，为普通闰年（如2004年、2020年就是闰年）。

世纪闰年：公历年份是整百数的，必须是400的倍数才是世纪闰年（如1900年不是世纪闰年，2000年是世纪闰年）。

闰年（Leap Year）是为了弥补因人为历法规定造成的年度天数与地球实际公转周期的时间差而设立的。补上时间差的年份为闰年。闰年共有366天（1-12月分别为31天、29天、31天、30天、31天、30天、31天、31天、30天、31天、30天、31天）。

凡阳历中有闰日（2月为29日）的年；闰余（岁余置闰。阴历每年与回归年相比所差的时日）。

注意闰年（公历中名词）和闰月（农历中名词）并没有直接的关联，公历中只分闰年和平年，平年有365天，而闰年有366天（2月中多一天）；平年中也可能有闰月（如2017年是平年，农历有闰月，闰6月）。

代码：
```python
for year in range(1700, 2022):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print('{} 是闰年'.format(year))
    else:
        print('{} 是平年'.format(year))
```
示例: [点我查看python代码](python/algorithm/leapyear.py "闰年")

***

## 百鸡百钱

我国古代数学家张丘建在《算经》一书中提出的数学问题：鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？

代码：
```python
for i in range(1, 21):
    for j in range(1, 34):
        k = 100 - i - j
        if (i*5 + j*3 + k/3) == 100 and k % 3 == 0:
            print('鸡翁: {} 鸡母: {} 鸡雏: {}'.format(i, j, k))
```
示例: [点我查看python代码](python/algorithm/100buy.py "百鸡百钱")

***

## 八皇后

在8×8格的国际象棋上摆放8个皇后，使其不能互相攻击，即任意两个皇后都不能处于同一行、同一列或同一斜线上，问有多少种摆法。

示例: [点我查看python代码](python/algorithm/eightqueens.py "八皇后")

***

## 汉诺塔

汉诺塔问题源于印度一个古老传说。相传大梵天创造世界的时候做了三根金刚石柱子，在一根柱子上从下往上按照大小顺序摞着64片黄金圆盘。大梵天命令婆罗门把圆盘从下面开始按大小顺序重新摆放在另一根柱子上。并且规定，任何时候，在小圆盘上都不能放大圆盘，且在三根柱子之间一次只能移动一个圆盘。问应该如何操作？  

代码:
```python
def move(n, a, b, c):
    if n == 1:
        print('{} --> {}'.format(a, c))
    else:
        move(n-1, a, c, b)
        print('{} --> {}'.format(a, c))
        move(n-1, b, a, c)


move(3, 'A', 'B', 'C')
```
示例: [点我查看python代码](python/algorithm/hanoi.py "汉诺塔")

***

## 水仙花数

水仙花数（Narcissistic number）也被称为超完全数字不变数（pluperfect digital invariant, PPDI）、自恋数、自幂数、阿姆斯壮数或阿姆斯特朗数（Armstrong number），水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身（例如：1^3 + 5^3+ 3^3 = 153）。

代码:
```python
for i in range(100, 1000):
    # 个位
    units = i % 10
    # 十位
    tens = int(i / 10) % 10
    # 百位
    hundreds = int(i / 100) % 10
    # 3次幂之和等于它本身，python中幂使用 **
    if (units ** 3 + tens ** 3 + hundreds ** 3) == i:
        print('{} 是水仙花数'.format(i))
```
示例: [点我查看python代码](python/algorithm/narcissisticnumber.py "水仙花数")

***

## 斐波那契数列

斐波那契数列又因数学家莱昂纳多·斐波那契以兔子繁殖为例子而引入，故又称为“兔子数列”。
一般而言，兔子在出生两个月后，就有繁殖能力，一对兔子每个月能生出一对小兔子来。如果所有兔子都不死，那么一年以后可以繁殖多少对兔子？

代码:
```python
def fibonacci(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fibonacci(12)
```
示例: [点我查看python代码](python/algorithm/fibonacci.py "斐波那契数列")

***

## 冒泡排序

它重复地走访过要排序的元素列，依次比较两个相邻的元素，如果顺序（如从大到小、首字母从Z到A）错误就把他们交换过来。走访元素的工作是重复地进行直到没有相邻元素需要交换，也就是说该元素列已经排序完成。

这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端（升序或降序排列），就如同碳酸饮料中二氧化碳的气泡最终会上浮到顶端一样，故名“冒泡排序”。

具体算法描述如下：

1. 比较相邻的元素。如果第一个比第二个大，就交换它们两个
2. 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，这样在最后的元素应该会是最大的数
3. 针对所有的元素重复以上的步骤，除了最后一个
4. 重复步骤1~3，直到排序完成

代码：
```python
arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]

for i in range(len(arr), 0, -1):
    for j in range(0, i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print('排序后结果: {}'.format(arr))
```
示例: [点我查看python代码](python/algorithm/bubblesort.py "冒泡排序")

***

## 快速排序

通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。

具体算法描述如下：

1. 从数列中挑出一个元素，称为 "基准"（pivot）
2. 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作
3. 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序

代码：
```python
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
```
示例: [点我查看python代码](python/algorithm/quicksort.py "快速排序")

***

## A Star

***