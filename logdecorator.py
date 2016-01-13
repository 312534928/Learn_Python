import time
import functools

ISOTIMEFORMAT = '%Y-%m-%d %X'


def log(arg):
	text = '' if hasattr(arg, '__call__') else arg

	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print('begin %s %s:' % (text, func.__name__))
			func(*args, **kw)
			print('end %s %s:' % (text, func.__name__))

		return wrapper

	return decorator(arg) if hasattr(arg, '__call__') else decorator


@log('excute')
# @log
def now():
	print(time.strftime(ISOTIMEFORMAT, time.localtime()))


now()
print(now.__name__)
