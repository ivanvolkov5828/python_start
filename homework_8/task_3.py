from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args):
        name_func = func.__name__
        variable = str(*args)
        type_variable = type(*args)
        return f"{name_func}({variable}: {type_variable})"
    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
print(a)
