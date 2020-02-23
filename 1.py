import timeit
import time

t = 0
n = 0


def average_time():
    global t
    global n

    def inner_decorator(func):
        global t
        global n

        def wrapper(a):
            global t
            global n
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
