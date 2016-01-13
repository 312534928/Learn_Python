import itertools
import time

a=int(input())
natuals=itertools.count(1)
for n in natuals:
	print(n)
	if n>=a:
		break
		