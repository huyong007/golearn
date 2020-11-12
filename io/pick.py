import pickle
d = dict(name='Bob', age=20, score=88)
pickle.dumps(d)
f = open('dump.txt', 'wb')

pickle.dump(d, f)

f.close()


