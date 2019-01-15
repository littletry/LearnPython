# _*_ coding: UTF-8 _*_

# 使用slots
# 如果我们想要限制class的属性怎么办？比如，只允许对Student实例添加name和age属性。
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class能添加的属性


class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


s = Student()  # 创建新的实例
s.name = 'littletry'  # 绑定属性'name'
s.age = 23  # 绑定属性'age'
s.score = 99  # 绑定属性'score'

# 由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。
# 使用__slots__要注意，__slots__定义的属性仅对当前类起作用，对继承的子类是不起作用的

