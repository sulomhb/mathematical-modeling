import math # vi trenger dette biblioteket senere
A_t1 = 2.00  # Tank 1 tverrsnittareal (m^2)
A_t2 = 2.00  # Tank 2 tverrsnittareal (m^2)
A_h1 = 0.002 # Hull 1 tverrsnittareal (m^2)
A_h2 = 0.002 # Hull 2 tverrsnittareal (m^2)
h_1 = 4.00 # Vannivået i tank 1 når forsøket starter (m)
h_2 = 4.00 # Vannivået i tank 2 når forsøket starter (m)
g = 9.81 # Gravitasjonskonstanten (m/s^2)
q_inn1 = 0.0025 # Mengde vann inn i toppen av tanken (m^3/s)
q_inn2 = 0 # initialverdi for innstrømming i tank 2
C = 0.61
k = C * math.sqrt(2*g)
print("Konstanten k er {}".format(k))
def euler(h, dh, dt):
    '''Regner ut ny høyde i tanken vet tiden t+dt, 
    gitt høyden og stigningstallet dh ved tiden t.'''
    return h + dh * dt
def stigning(A_h, A_t, h, q_inn):
    '''Regner ut stigningen i punktet h.
    Parameteren k er en global konstant.'''
    return 1/A_t * ((q_inn) - A_h * k * math.sqrt(h))
def hastighet(h):
    '''Regner ut hastigheten til væskestrømmen ut av tanken 
    når væskehøyden er h. Parameteren k er en global konstant.'''
    if h > 0.0:
        return k * math.sqrt(h)
    else:
        return 0.0
t = 0  # starttiden
dt = 60 # tidssteg i sekunder
h_lim = 0.01 # vi stopper beregningen når høyden er mindre enn denne
t_lim = 10000 # vi stopper beregningen etter 4800 sekunder
t_hist = [] # Lagerplass for historiske tidspunkter
h1_hist = [] # Lagerplass for historiske h-verdier
h2_hist = [] # Lagerplass for historiske h-verdier
while h_1 > h_lim and t < t_lim:
    if t > 0: # ingen beregning ved t = 0, der bruker vi initialverdier
        h_1 = euler(h_1, stigning(A_h1, A_t1, h_1, q_inn1), dt)
        v_1 = hastighet(h_1) # Hastigheten til væsken som strømmer ut av hullet
        q_inn2 = A_h1 * v_1 # Mengden væske som strømmer ut av hullet i tank 1
        h_2 = euler(h_2, stigning(A_h2, A_t2, h_2, q_inn2), dt)
    print("t = {} => h_1 = {} \t q_inn1 = {} \t h_2 = {} \t q_inn2 = {}".format(t, round(h_1,2), q_inn1, round(h_2,2), round(q_inn2,4)))
    t_hist.append(t)
    h1_hist.append(h_1)
    h2_hist.append(h_2)
    t += dt
import matplotlib.pyplot as plt
plt.plot(t_hist, h1_hist, label="Tank 1")
plt.plot(t_hist, h2_hist, label="Tank 2")
plt.ylabel('Høyde [m]')
plt.xlabel('Tid [s]')
plt.axis([0, t_lim, min(h1_hist + h2_hist)*0.9, max(h1_hist + h2_hist)*1.1])
plt.legend()
plt.grid()
plt.show()