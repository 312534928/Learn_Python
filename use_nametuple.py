from collections import namedtuple
Point = namedtuple('Point',['x','y'])
p=Point(1,2)
print(p.x,"and",p.y)
Circle = namedtuple('Circle',['x','y','r'])
c=Circle(1,2,3)
print(c.x,c.y,c.r)