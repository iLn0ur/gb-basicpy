def val_checker(bool_arg):
    def real_val_check(func):
        def wrapper(x):
            if bool_arg(x):
                return func(x)
            else:
                raise ValueError(f'wrong value: {x}')
        return wrapper
    return real_val_check


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(-15))
