import heapq


# 根据给定优先级进行排序，并且每次pop操作都返回优先级最高的元素的队列例子。

class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Item({!r})".format(self.name)


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def __str__(self):
        return "{!r}".format(self._queue)

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        pop = heapq.heappop(self._queue)[-1]
        self._index -= 1
        return pop


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
q.push(Item('naa'), 3)
q.push(Item('lala'), 7)
print(q)
print(q.pop())

print(q)
