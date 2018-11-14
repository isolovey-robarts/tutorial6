def function1():
    return 4

def function2(x):
    return x*x

def function3(x, y):
    return x-y*y+5


def main():
    print function1() - function2(5) + function3(6,7)

