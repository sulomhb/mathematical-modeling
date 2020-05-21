import numpy as np
import matplotlib.pyplot as plt
import math

# Oppgave 1 - funksjoner for x- og y-posisjon
def rx(t):
    '''Ballens posisjon som funksjon av tid i x-retning'''
    return 5 + 31*t - 3*t**2

def ry(t):
    '''Ballens posisjon som funksjon av tid i y-retning'''
    return 12*t - 5*t**2

# Oppgave 2 - deriverer for å finne fart fra endring i posisjon
def derivert(f, x, dx):
    '''Beregning av den deriverte til funksjonen f i punktet x.
       Bruker Newtons kvotient.'''
    return (f(x+dx) - f(x))/dx

# Oppgave 3 - finner fart ved t = 0
vx_start = derivert(rx, 0, 1E-12)
vy_start = derivert(ry, 0, 1E-12)
print("Oppgave 3:", vx_start, vy_start)

# Oppgave 4 - finner banefart ved t = 0
v_bane_start = math.sqrt(vx_start**2 + vy_start**2) # Pythagoras
print("Oppgave 4:", v_bane_start)

# Tids-array. Fant passende slutt-tid i oppgave 5
t = np.arange(0, 2.41, 0.01) 

# Regner ut x og y for alle t
x = rx(t)
y = ry(t)

# Finner største ballhøyde, ikke brukt i noen av oppgavene...
t_y_max = np.where(y == y.max()) # Høyeste punkt i ballbanen
print("Bonus... Maks ballhøyde:", y[t_y_max][0])

# Oppgave 5 - finner ut hvor ballen treffer bakken
t_y_min = np.where(y == 0) # Ballen er på bakken når y = 0
print("Tidspunktet hvor ballen treffer bakken:", t_y_min)
print("Oppgave 5:", x[t_y_min][1] - 5) # Husk å trekke fra 5 meter!

plt.plot(x, y)
plt.xlabel("lengde (m)")
plt.ylabel("høyde (m)")
plt.axhline(linewidth=1.5, color="black")
plt.axvline(linewidth=1.5, color="black")
# Spør ikke om at aksene har samme skala i denne oppgava, 
# men kunne gjort det slik:
#plt.xlim(-1, 65)
#plt.ylim(-1, 65)
plt.grid()
plt.title("Oppgave 6")
plt.show()