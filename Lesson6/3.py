class slovar:
    a = []
    b = []

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def func(a, b):
        for i in range(a):
            yield b[i] if i < a else None
