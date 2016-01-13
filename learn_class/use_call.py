class Next:
    List = []

    def __init__(self, low, high):
        for Num in range(low, high):
            self.List.append(Num ** 2)

    def __call__(self, Nu):
        return self.List[Nu]


if __name__ == '__main__':
    b = Next(1, 7)
    print(b.List)
    print(b(2))
