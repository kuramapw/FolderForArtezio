def gen_squares(obj):
    s = [arg for arg in dir(obj) if not arg.startswith('_')]
    for i in s:
        yield i
