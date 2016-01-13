# 二叉堆一般用数组来表示。例如，根节点在数组中的位置是0，第n个位置的子节点分别在2n+1和 2n+2。因此，第0个位置的子节点在1和2，1的子节点在3和4。以此类推。这种存储方式便於寻找父节点和子节点。
import heapq

heap = []

for value in [20, 30, 26, 12, 7, 46]:
    heapq.heappush(heap, value)

print(heap)

heapq.heappush(heap, 5)
print(heap)

print(heapq.heappop(heap))
print(heap)

print(heapq.nlargest(2, heap))
print(heapq.nsmallest(2, heap))

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(2, portfolio, key=lambda x: x['price'])
expensive = heapq.nlargest(2, portfolio, key=lambda x: x['price'])

print(cheap)
print(expensive)
