from functools import wraps
def hello(func):
    @wraps(func)
    def wrapper():
        print('hello,%s' % func.__name__)
        func()
        print('goodbye,%s' % func.__name__)

    return wrapper

@hello
def foo():
    print("i'm foo")

foo()

print(foo.__name__)