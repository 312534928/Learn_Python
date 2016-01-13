class Sample:
    def __enter__(self):
        print("In __enter__()")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):  # 开发库时，清理资源，关闭文件等等操作，都可以放在__exit__方法当中。
        print("In __exit__()")
        print("type:", exc_type)
        print("value:", exc_val)
        print("trace:", exc_tb)

    def do_something(self):
        print("In do_something() ")
        bar = 1 / 0
        return bar + 10


# a=Sample()
# a.do_something()
#
# a=Sample
# a.do_something

with Sample() as sample:
    sample.do_something()
