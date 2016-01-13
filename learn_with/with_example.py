class Sample:
    def __enter__(self):
        print("In __enter__()")
        return "Foo"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("In __exit__()")


def get_sample():
    return Sample()


# sample 此时为被函数赋值的变量
with get_sample() as sample:
    print("sample:", sample)
