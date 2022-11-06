from functools import update_wrapper, wraps


class TypeValidator:

    def __init__(self, arg_type):
        print('Here arg from decorator:', arg_type)
        self.arg_type = arg_type

    def __call__(self, func):
        print("Here function name:", func.__name__)
        self.func = func

        @wraps(self.func)
        def wrapper(*args, **kwargs):
            print('Here arg from function:', args)
            if not all([isinstance(arg, self.arg_type) for arg in args]):
                raise TypeError(f'All parameters need to be {self.arg_type}!')
            else:
                return self.func(*args)
        return wrapper


@TypeValidator(str)
def joiner(*params):
    return " ".join(params)


if __name__ == "__main__":
    print(joiner('c', 'b', 'c'))