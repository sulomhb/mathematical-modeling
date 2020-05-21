import math 
def f(x):
    return math.sin(x) - (1/2)
def derivert(f, x, dx):
    return (f(x+dx) - f(x)) / dx 
def neste_x(f, x, dx):
    return x - f(x)/derivert(f, x, dx)
TOL = 1E-9
x = 0
x_neste = 1
while abs(x - x_neste) > TOL:
    x = x_neste
    x_neste = neste_x(f, x, 1E-12)
print(x_neste)