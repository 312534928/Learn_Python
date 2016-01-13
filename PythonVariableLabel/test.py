a = [1, 2, 3]
b = a
print(id(a))
print(id(b))

a[1] = a
# 输出是 [1,[1,2,3],2,3]？？
print(a)

a = [1, 2, 3]
a[1] = a[:]
# 先 dereference 得到 values 所指向的对象 [0, 1, 2]，然后执行 [0, 1, 2][:] 复制操作得到一个新的对象，
# 内容也是 [0, 1, 2]，然后将 values 所指向的列表对象的第二个元素指向这个复制二来的列表对象，
# 最终 values 指向的对象是 [0, [0, 1, 2], 2]
# 浅复制(shallow copy),它复制了对象,但对于对象中的元素,依然使用引用
print(a)

# shallow copy
a = [0, [1, 2], 3]
b = a[:]
a[0] = 8
a[1][1] = 9
print(a)
print(b)

# deep copy
import copy

a = [0, [1, 2], 3]
b = copy.deepcopy(a)
a[0] = 8
a[1][1] = 9
print(a)
print(b)
