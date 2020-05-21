from matplotlib import pyplot as plt
def L(v):
    'Dette gir |luftmotstandkraften| (N)'
    return k * v**2 # L = kv^2 er en "grei" modell for luftmotstand
# Tidssteg
dt = 0.001 # dette er hvor ofte høyde- og fartsverdiene vil oppdateres (s)
# Fysiske konstanter
m = 91 # massen til fallskjermshopperen (kg)
g = 9.81 # |gravitasjonakselerasjonen| (m/s)
k = 0.24 # luftmotstandkonstanten (kg/m)
# Lister for tid, høyde, og fart. Nødventig å ha noen verdier hvis du skal plotte!
t_verdier = [] # tidsverdier (s)
h_verdier = [] # høyde-over-bakken-verdier (m)
v_verdier = [] # |fart|sverdier (m/s)
# Startbetingelser
t = 0 # starttid (s)
h = 3000 # starthøyde over bakken (m)
v = 0 # |startfart| (m/s)

# Eulers metode
while h > 0: # vi kjører denne mens fallskjermshopperen er over bakken; etter det er vi ferdige.
    t_verdier.append(t) # setter inn den nåverdige tidsverdien i listen
    h_verdier.append(h) # setter inn den nåverdige høydeverdien i listen
    v_verdier.append(v) # setter inn den nåverdige fartsverdien i listen
    a = g - L(v) / m # utregning av |akselerasjon|. Luftmotstanden L er en kraft, derfor må vi dele den på massen.
    v += a * dt # numerisk integrasjon av |akselerasjon| til |fart|
    h -= v * dt # numerisk integrasjon av |fart| til posisjon
    t += dt # fullfør tidssteg

# Skriving ut av resultater
print(f'Det tar ca. {t:.2f} sekunder før du treffer bakken med en fart på ca. {v:.2f} m/s.') # se på hvordan en streng bør formateres!

fig, ax1 = plt.subplots()
ax1.set_title(f'Masse = {m} kg')
farge = 'tab:blue'
ax1.set_xlabel('Tid (s)')
ax1.set_ylabel('Høyde over bakken (m)', color=farge)
ax1.plot(t_verdier, h_verdier, color=farge)
ax2 = ax1.twinx()
farge = 'tab:red'
ax2.set_ylabel('|Fart| (m/s)', color=farge)
ax2.plot(t_verdier, v_verdier, color=farge)
plt.show()
