# _*_ coding: UTF-8 _*_

# type()函数既可以返回一个对象的类型，又可以创建出新的类型，
# 比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义：


def fn(self, name = 'world'):    # 先定义函数
    print('Hello, %s.' % name)


Hello = type('Hello', (object,), dict(hello=fn))  # 创建Hello class

h = Hello()

h.hello()

print type(Hello)

print type(h)


# 要创建一个class对象，type()函数依次传入3个参数：
#
# class的名称；
# 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。


# 通过type()函数创建的类和直接写class是完全一样的，
# 因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。


