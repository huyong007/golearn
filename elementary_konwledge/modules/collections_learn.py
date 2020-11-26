
from collections import namedtuple, deque, defaultdict, OrderedDict


Point = namedtuple('Point', ['x', 'y'])

p = Point(1, 2)

print(p.x, p.y)


print(type(p))
print(isinstance(p, tuple))


Circle = namedtuple('Circle', ['x', 'y', 'r'])

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')

print(q)

q.pop()
print(q)
q.popleft()
print(q)

dd = defaultdict(lambda: 'N/A')

dd['key1'] = 'abc'

print(dd['key1'])

print(dd['key2'])

d = dict([('a', 1), ('b', 2), ('c', 3)])

print(d)

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)


class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            print(containsKey, 'containsKey')
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)


ludict = LastUpdatedOrderedDict(3)

ludict['a'] = 2
ludict['b'] = 3
ludict['c'] = 4
ludict['e'] = 5
ludict['b'] = 5
ludict.setitem('d', 0)
print(ludict)
