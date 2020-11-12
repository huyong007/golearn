
import pickle
f = open('homework.py', 'rb')
d = pickle.load(f)
f.close()
print(d)
