# _*_ coding: UTF-8 _*_

# __str__


class Student1(object):
    def __init__(self, name):
        self.name = name


class Student2(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name
    __repr__ = __str__

# __str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，
# 也就是说，__repr__()是为调试服务的。


print Student1('LittleTry')
print Student2('LittleTry')
