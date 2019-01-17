# _*_ coding: UTF-8 _*_
# list有个神奇的切片方法


print range(100)[5:10]

# 对于Fib却报错。原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断


class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            a, b = 1, 1
            l = []
            for x in range(stop):
                if x >= start:
                    l.append(a)
                a, b = b, a + b
            return l


f = Fib()
print f[6:22]
print f[:12]


# 但是没有对step参数作处理：
print f[:10:2]

# 也没有对负数作处理，所以，要正确实现一个__getitem__()还是有很多工作要做的。
