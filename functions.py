def transform_data(fn, *args):
    for arg in args:
        print('Result: {result:^20.2f} {extra}'.format(
            result=fn(arg), extra=20))


transform_data(lambda data: data / 5, 10, 15, 22, 30)
