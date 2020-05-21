import numpy as np

def f(x, k): #f(x)
    return k*x**3 + k*x**2 + 3/4 *k*x + 1
x = 3/4 # Bestemt i oppgaven
lst_k = np.arange(-10, 10, 1E-4) # K - verdier fra -10 til 10
for k in lst_k: # Sjekker ulike k -verdier
    if f(x,k) > 0 and f(x,k) < 1E-4: # Sjekker når f(x) = så nærme 0 så mulig.
        print("x = {}".format(x)) 
        print("k = {}".format(k))
    continue

