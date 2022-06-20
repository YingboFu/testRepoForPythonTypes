
def foo2(a: int, b: int) -> int:
    return a * b

def foo(a: int, b: int) -> int:
    c = 0
    return a + b + c


if __name__ == '__main__':
    print(foo(1, 2))
    print(foo2(3, 4))
