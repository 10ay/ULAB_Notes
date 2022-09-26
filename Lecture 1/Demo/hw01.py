from operator import add, sub

def a_plus_abs_b(a, b):
    if b < 0:
        f = a-b
    else:
        f = a+b
    return f(a, b)
