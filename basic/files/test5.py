# -*- coding: UTF-8 -*-

# 打开一个文件
fo = open("foo.txt", "r+")
str1 = fo.read(10)
print "读取的字符串是 : ", str1
# 关闭打开的文件
fo.close()
