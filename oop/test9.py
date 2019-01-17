# _*_ coding: UTF-8 _*_

# 正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。
# 调用name属性，没问题，但是，调用不存在的score属性，就有问题了：
# >>> s = Student()
# >>> print s.name
# Michael
# >>> print s.score
# Traceback (most recent call last):
#   ...
# AttributeError: 'Student' object has no attribute 'score'

# 要避免这个错误，除了可以加上一个score属性外，Python还有另一个机制，
# 那就是写一个__getattr__()方法，动态返回一个属性。


class Student(object):

    def __init__(self):
        self.name = 'LittleTry'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99

# 当调用不存在的属性时，比如score，
# Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性，这样，我们就有机会返回score的值：


s = Student()
print s.name
print s.score

# 返回函数也是完全可以的：


class Student2(object):

    def __getattr__(self, attr):
        if attr == 'age':
            return lambda: 23


# 只是调用方式要变为：
s = Student2()
print s.age()

# 注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。

# 此外，注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。
# 要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误：


class Student3(object):

    def __getattr__(self, attr):
        if attr == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
