# 构造从3开始的奇数序列
def _odd_iter():
	n = 1
	while True:
		n += 2
		yield n


# 筛选函数
def _not_divisible(n):
	return lambda x: x % n > 0


def primes():
	yield 2
	it = _odd_iter()
	while True:
		n = next(it)
		yield n  # 生成器调用next的时候执行，yield时返回，再次调用时从这个yield继续执行
		it = filter(_not_divisible(n), it)


for n in primes():
	if n < 1000:
		print(n)
	else:
		break
