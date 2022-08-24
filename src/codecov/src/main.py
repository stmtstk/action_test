""" Test for main module """

def func_1(a_int: int) -> int:
    """ func_1 """
    #print(f'Enter func_1 ({a_int})')
    return a_int

def func_2(a_int: int) -> int:
    """ func_2 """
    #print(f'Enter func_2 ({a_int})')
    return a_int

def main(cond_1: bool,cond_2: bool) -> None:
    """ main """
    #print(f'Enter main (cond_1: {cond_1})')
    #print(f'Enter main (cond_2: {cond_2})')
    if cond_1:
        func_1(10)
    if cond_2:
        func_2(20)

if __name__ ==  '__main__':
    main(False, True)
