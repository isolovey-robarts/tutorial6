def function1():
    """simple function"""
    return 5

def function2(x):
    """square a number"""
    return x*x

def function5(x,y,z):
    """multiply and subtract"""
    return x*y*z-3

def main():
    "print linear combination"
    print function1() - function2(5) + function5(1,2,3)

