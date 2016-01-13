a = 1
print("Before the function")
print("Value a:%d  Address of a:%d" % (a, id(a)))


def func1(a):
    a += 4
    print("In the function,")
    print("Value a:%d  Address of a:%d" % (a, id(a)))


func1(a)
print("Out of the function")
print("Value a:%d  Address of a:%d" % (a, id(a)))


print("__________________________________________")
a = 2
print("Before the function")
print("Value a:%d  Address of a:%d" % (a, id(a)))


def func2():
    global a
    print("In the function,")
    print("Value a:%d  Address of a:%d" % (a, id(a)))
    a+= 4
    print("After the a+= 4")
    print("Value a:%d  Address of a:%d" % (a, id(a)))


func2()

print("After the function")
print("Value a:%d  Address of a:%d" % (a, id(a)))


def functest(a):
    b = a
    a = a + 1
    print(b)


functest(a)

c = 2


def func():
    global c
    c = c + 1


func()
print(c)
