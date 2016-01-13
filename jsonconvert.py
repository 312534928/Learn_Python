import json

d = dict(name='Leon', age=23, score=99)
a = json.dumps(d)
print(type(d))
print(type(a))
c = json.loads(a)
print(type(c))
