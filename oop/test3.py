# _*_ coding: UTF-8 _*_


class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2014 - self._birth

# 上面的birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。
