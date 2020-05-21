import matplotlib.pyplot as plt 
import numpy as np 
def f(x):
    '''Definerer funksjonen x^3 + 3x^2 + x - 1'''
    return x**3 + 3*x**2 + x - 1
def f_der(x):
    '''Den deriverte av funksjonen ovenfor, analytisk løsning.
       Bruker denne for å sammenlikne med numerisk løsning.'''
    return 3*x**2 + 6*x + 1
def deriv(f, x, h):
    '''Funksjon for å beregne den deriverte av en funksjon
       Newtons kvotient'''
    return (f(x+h) - f(x)) / h
def symderiv(f, x, h):
    '''Funksjon for å beregne den deriverte av en funksjon
       Newtons symmetriske kvotient'''
    return (f(x+h) - f(x-h)) / 2*h
dx = [10**-i for i in range(1, 20)] # Liste med dx fra 10^-1 til 10^-20
for h in dx:
    print(deriv(f, 0.0, h)) # Regner ut den deriverte for x=0 med ulike dx

x = np.arange(-3, 1, 0.1) # Lager en array med x-verdier
y = f(x) # Regner ut funksjonsverdier for alle x-verdiene
y_der = f_der(x) # Regner ut den deriverte (analytisk svar)
y_der_newton = deriv(f, x, 1E-10) # Numerisk svar
# Resten er plotting av svaret :-)
plt.plot(x, y)
plt.plot(x, y_der)
plt.scatter(x, y_der_newton, marker="X", color="r")
plt.xlabel("x-verdier")
plt.ylabel("y-verdier")
plt.title("Tredjegradsfunksjon")
plt.grid()
plt.axhline(linewidth=1.5, color="black")
plt.axvline(linewidth=1.5, color="black")
plt.show()