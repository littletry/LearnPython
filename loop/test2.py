# -*- coding: UTF-8 -*-
"""
在 python 中，for … else 表示这样的意思，
for 中的语句和普通的没有区别，
else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行，
while … else 也是一样。
"""

for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0:
            j = num / i
            print '%d 等于 %d * %d' %(num, i, j)
            break
    else:
        print num, '是一个质数'
