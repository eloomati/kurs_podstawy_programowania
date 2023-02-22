
def date(a):
    d = type(a)
    if d == int or d == float or d == complex:
        print("Wprowadzony parametr jest typu liczbowego")
    else:
        print("Wprowadzony parametr jest obiektem iterowalnym")

date(1)

def fun(thing):
    if type(thing) in [tuple,list,bytes,str]:
        print("Wprowadzony parametr jest obiektem iterowalnym")
    elif type(thing) in [complex,float,int]:
        print("Wprowadzony parametr jest typu liczbowego")


fun(1)

def f(x):
    if type(x) == str or type(x) == list or type(x) == tuple:
        print("Wprowadzony parametr jest obiektem iterowalnym")

    elif type(x) == int or type(x) == float or type(x) == complex:
        print("Wprowadzony parametr jest typu liczbowego")
f("a")
f((1,2))
f(1)
f(3.4)