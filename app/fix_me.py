def max_number(a: int, b: int) -> int:
    if a > b:
        return a
    else:
        return b


def multiply(a: int, b: int) -> int:
    return a * b


class FixMe:
    def __init__(self, name: str) -> None:
        self.name = name

    @staticmethod
    def zero_function(x: int) -> None:
        if x > 0:
            print("positive")
        elif x < 0:
            print("negative")
        else:
            print("zero")
