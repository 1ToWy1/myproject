def max_number(a, b):
    if a > b:
        return a
    else:
        return b


def multiply(a, b):
    return a * b


class FixMe:
    def __init__(self, name):
        self.name = name


    @staticmethod
    def zero_function(x):
        if x > 0:
            print("positive")
        elif x < 0:
            print("negative")
        else:
            print("zero")
