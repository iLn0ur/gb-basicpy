def type_logger(func):
    def wrapper(*args):
        if len(args) == 1:
            return f'{func.__name__} - {type(func(args[0]))} ({args[0]}:{type(args[0])}), result={func(args[0])} '
        else:
            type_args = [type(a) for a in args]
            return f'{func.__name__}({type_args})'
    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


print(calc_cube(5))
