from functools import wraps
import time


def time_it(repeat_num=1):
    def outer_wrapper(func):
        @wraps(func)
        def inner_wrapper(*args, **kwargs):
            start_time = time.time()
            for _ in range(repeat_num):
                func(*args, **kwargs)
            stop_time = time.time()
            elapsed_time = stop_time - start_time
            print(f'Function "{func.__name__}" called {repeat_num} times. Elapsed time: {elapsed_time:0.3f}s')
            return func(*args, **kwargs)
        return inner_wrapper
    return outer_wrapper


@time_it(1000000)
def example_func(arg):
    return arg ** arg

if __name__ == "__main__":
    print('Result:', example_func(5))
