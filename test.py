from types import MethodType


class Student(object):
    __slots__ = ('name','age')


s = Student()

s.name = 'Michael'
s.age = 25

class GraduateStudent(Student):
    pass

g = GraduateStudent()

g.score = 999
