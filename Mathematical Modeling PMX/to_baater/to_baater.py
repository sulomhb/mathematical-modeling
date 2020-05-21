import math
# Baat A
def xpos_a(t):
  return 18*t - 8

def ypos_a(t):
  return 10-3*t

# Baat B
def xpos_b(t):
  return 10*t

def ypos_b(t):
  return 20 - 6*t

# Derivert
def deriv(f, x, h):
    return (f(x+h) - f(x)) / h

dt = 0.01

# Oppgave A - Finn banefarten til baatene.
banefart_baat_a = math.sqrt(deriv(xpos_a, 1, dt)**2  + deriv(ypos_a, 1, dt)**2)
banefart_baat_b = math.sqrt(deriv(xpos_b, 1, dt)**2  + deriv(ypos_b, 1, dt)**2)
print('Banefarten til baat A er: %f ' %(banefart_baat_a))
print('Banefarten til baat B er: %f ' %(banefart_baat_b))

#Oppgave B - Avstand mellom baater.
# Avstanden mellom to punkt er det samme som lengden av vektoren mellom punktene.
# Vi har Baat A(xpos_a, ypos_a) og Baat B(xpos_b, ypos_b)
# Vektoren mellom disse er:  [Baat A] - [Baat B]
# Dermed er avstanden d:
avstand_mellom_baatene = math.sqrt((xpos_a(1) - xpos_b(1))**2 + (ypos_a(1) - ypos_b(1))**2)
# I oppgaven:
# Vi sier t = 1.
avstand_mellom_baatene_i_oppgaven = math.sqrt((8*1-8)**2 + (3*1 - 10)**2)

print('Losningen paa avstanden mellom baatene i oppgaven er: %f' %(avstand_mellom_baatene_i_oppgaven))
print('Bevis for at vi finner samme ut av samme avstand mellom baatene: %f' %(avstand_mellom_baatene))

#Oppgave C: 
# [AB] = [8t - 8 , -10 + 3t]

