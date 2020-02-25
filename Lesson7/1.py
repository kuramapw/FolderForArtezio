import timeit
import time


def average_time():
    t=0
    n=0

    def inner_decorator(func):

        def wrapper(a):
            nonlocal t
            nonlocal n
            t = t + a
            n = n + 1
            print(t / n)
            return t / n

        return wrapper

    return inner_decorator


@average_time()
def func(a):
    time.sleep(a)
    return a


func(5)
func(4)
