class cycle:
    def __iter__(self):
        return self

    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter == self.limit:
            self.counter = 0
        if self.counter < self.limit:
            self.counter += 1
            return self.counter
        else:
            raise StopIteration


def gen_squares(n):
    s = [arg for arg in cycle(n)]
    for i in s:
        yield i
