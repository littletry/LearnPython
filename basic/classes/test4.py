# -*- coding: UTF-8 -*-


class Employee:
    """所有员工的基类"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.name, ", Salary: ", self.salary


"创建 Employee 类的第一个对象"
emp1 = Employee("Zara", 2000)
"创建 Employee 类的第二个对象"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount

emp1.age = 7  # 添加一个 'age' 属性
emp1.age = 8  # 修改 'age' 属性
del emp1.age  # 删除 'age' 属性

hasattr(emp1, 'age')     # 如果存在 'age' 属性返回 True。
getattr(emp1, 'age')     # 返回 'age' 属性的值
setattr(emp1, 'age', 8)  # 添加属性 'age' 值为 8
delattr(emp1, 'age')     # 删除属性 'age'
