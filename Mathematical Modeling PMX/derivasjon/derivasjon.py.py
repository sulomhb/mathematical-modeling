import numpy as np
import matplotlib.pyplot as plt

dx = 1E-5

def derivert(f, x):
  return (f(x + dx) - f(x)) / dx

def andrederivert(f, x):
  return (f(x + 2*dx) - 2*f(x + dx) + f(x)) / dx**2

def f(x):
    return (x + 1) / (x**2 + 1)

x = np.arange(-2.0, 2.0, dx)

funk = f(x)

deriv = derivert(f,x)

dobbel = andrederivert(f, x)

fig, ax = plt.subplots()

ax.plot( x, funk, label='f(x)')
ax.plot( x, deriv, label="f'(x)")
ax.plot( x, dobbel, label="f''(x)")
ax.grid()

plt.legend() # viser navn på de ulike grafene

plt.show()
    
    
  
  
