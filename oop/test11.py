# _*_ coding: UTF-8 _*_

# 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。
# 能不能直接在实例本身上调用呢？类似instance()？在Python中，答案是肯定的。
# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。


class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)


s = Student('LittleTry')
s()


# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。


print callable(Student)
print callable(max)
print callable([1, 2, 3])
print callable('String')

