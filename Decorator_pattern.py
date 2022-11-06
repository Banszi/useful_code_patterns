from functools import wraps


def decorator_pattern(*decorator_args):
    print("Here decorator args:", decorator_args)
    def outer_wrapper(func):
        print("Here decorated function name:", func.__name__)
        @wraps(func)
        def inner_wrapper(*args, **kwargs):
            print("Here function args:", args)
            func_resuls =  func(*args, **kwargs)
            # Change function result inside decorator
            func_resuls += ' -additional text from decorator-'
            return func_resuls
        return inner_wrapper
    return outer_wrapper


@decorator_pattern('DECO_ARG')
def example_func(*func_args):
    return " ".join(func_args)


if __name__ == "__main__":
    print('Result:', example_func('-a-', '-b-', '-c-'))