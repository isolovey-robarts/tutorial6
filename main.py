def function1():
    return 5

def function2(x):
    return x*x

def function5(x,y,z):
    return x*y*z-3

def main():
    print function1() - function2(5) + function5(1,2,3)

