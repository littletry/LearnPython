# _*_ coding: UTF-8 _*_

# 链式调用


class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path


print Chain().status.user.timeline.list
