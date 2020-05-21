import numpy as np 
def f(x):
    '''

    '''
    return x**3 - 2*x**2 + 1
def halvering(f, a, b):
    while abs(a-b) > 1E-9:
        x = (a+b)/ 2
        if f(a)*f(x) < 0:
            b = x
        else:
            a = x 
    return x
a = 1 # velger et punkt før nullpunktet
b = 1.5 # Velger et punkt etter nullpunktet
print(halvering(f, a, b))