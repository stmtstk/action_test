
class PackageClass (object):

    def __init__(self) -> None:
        """ dummy __init__ """
        return

    def func_1(self, a_int: int) -> int:
        """ func_1 """
        print(f'Enter func_1 ({a_int})')
        return a_int

    def func_2(self, a_int: int) -> int:
        """ func_2 """
        print(f'Enter func_2 ({a_int})')
        return a_int
