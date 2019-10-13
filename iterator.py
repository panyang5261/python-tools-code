class MyRange:
    def __init__(self, n, start=0):
        self.value = n
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        num = self.start
        if num >= self.value:
            raise StopIteration
        self.start += 1
        return num


if __name__  == '__main__':
    mr = MyRange(10)
    for m in mr:
        print(m)

