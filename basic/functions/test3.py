# -*- coding: UTF-8 -*-

"""下例能将关键字参数顺序不重要展示得更清楚"""


# 可写函数说明
def printinfo(name, age):
    """打印任何传入的字符串"""
    print "Name: ", name
    print "Age ", age
    return


# 调用printinfo函数
printinfo(age=50, name="miki")
