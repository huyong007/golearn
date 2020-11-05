class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    pass


L = MyList()

L.add(1)
print(L)
print(L)


#   File "/Users/huyong/allfile/learn/python/class_learn/metaclass.py", line 7
#     class MyList(list, metaclass=ListMetaclass):
#                                 ^
# SyntaxError: invalid syntax