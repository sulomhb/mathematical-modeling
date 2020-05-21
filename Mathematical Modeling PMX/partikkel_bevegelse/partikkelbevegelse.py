import numpy as np
import matplotlib.pyplot as plt

# r(t) = [t^3-2*t , t^2 + 1]

def x(t):
    'x koordinaten'
    return t**3 - 2*t

def y(t):
    'y koordinat'
    return t**2 + 1

dt = 0.001

# t er i intervallet -2 og 2

t = np.arange(-2, 2, dt)
x_ver = x(t)
y_ver = y(t)
x_f = x(-1  )
y_f = y(-1)
banefart = np.sqrt(x_f**2 + y_f**2)
print('Banefarten er :', banefart)

# Graf

plt.plot(x_ver, y_ver)
plt.xlabel('Tid')
plt.ylabel('Fart gitt ved tid')
plt.show()

