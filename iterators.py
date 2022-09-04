#Iterators give only one value on each enter
#Iter will give you the iterator
#next will give you the next iterator


class TopTen:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self
    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration

values = TopTen()

for i in values:
    print(i)
