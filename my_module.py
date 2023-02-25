"""
Moduł 4 funkcji
"""

def summa(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a // b

if __name__ == "__main__":
    print("Test: ", summa(1, 2))
    print("Test: ", sub(3, 5), sub(10, 7))
    print("Test: ", mult(2, 3), mult(4, 5))
    print("Test: ", div(10, 5), div(1000, 30))