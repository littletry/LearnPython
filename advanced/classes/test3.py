# _*_ coding: UTF-8 _*_


from advanced.classes.test1 import Employee

"""创建 Employee 类的第一个对象"""
emp1 = Employee("Zara", 2000)

"""创建 Employee 类的第二个对象"""
emp2 = Employee("Manni", 5000)


emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount
