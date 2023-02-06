def meta(*args):
    print(args)


class A(metaclass=meta):
    z=40

