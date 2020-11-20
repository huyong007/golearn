import json
d = dict(name='Bob', age=20, score=88)

print(isinstance(json.dumps(d), str))
