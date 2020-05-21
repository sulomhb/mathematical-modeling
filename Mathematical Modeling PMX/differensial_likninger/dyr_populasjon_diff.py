from matplotlib import pyplot as plt
from math import exp


def derivative(F, D, M):
    'beskriver vekstfarten til befolkningen'
    return F - D - M

P = 500 # start populasjon
t_verdier = [] # i år
P_verdier = [] # vi skal plotte disse (hver måned)
for t in range(240): # mens det har gått mindre enn 20 år (240 måneder)
    t_verdier.append(t / 12) # slik at vi får grafen i år, ikke i måneder
    P_verdier.append(P)
    F = 0.3 * P # dette er F per år
    D = 0.25 * P # D per år
    M = exp(P / 200) # M per år
    P += derivative(F, D, M) / 12  # her er dt = 1/12 siden vi gjør beregninger hver måned
    
plt.xlabel("Tid (år)")
plt.ylabel("Antall individer")
plt.plot(t_verdier, P_verdier)
plt.show()