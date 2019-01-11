a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))


class A:
    pass


class B(A):
    pass


print(isinstance(A(), A))    # returns True
print(type(A()) == A)        # returns True
print(isinstance(B(), A))    # returns True
print(type(B()) == A)        # returns False

'''
isinstance 和 type 的区别
    type()不会认为子类是一种父类类型。
    isinstance()会认为子类是一种父类类型。
'''
