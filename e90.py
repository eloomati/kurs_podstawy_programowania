from math import e, pi

def fun(*args, **kwargs):
    print(args, kwargs)

fun(12, 14, x=0, y=1, pi=pi, e=e)