# -*- coding: UTF-8 -*-
"""
不定长参数
    你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述2种参数不同，声明时不会命名。
"""


def printinfo(arg1, *vartuple):
    """打印任何传入的参数"""
    print "输出: "
    print arg1
    for var in vartuple:
        print var
    return


# 调用printinfo 函数
printinfo(10)
printinfo(70, 60, 50)
