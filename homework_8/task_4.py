from functools import wraps


def val_checker(callback):
    def logger(func):
        @wraps(func)
        def wrapper(*args):
            result = func(*args)
            if callback(*args):
                return result
            else:
                raise ValueError(*args)
        return wrapper
    return logger


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(6)
print(a)
