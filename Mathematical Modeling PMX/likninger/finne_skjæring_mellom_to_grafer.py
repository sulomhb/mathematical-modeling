import numpy as np

# Hvis du skal sjekke g(x)=y(x), bare bytt ut g(x) og y(x). Det skal funke.
def g(x) : #graf 1
    return -3*x - 8
def h(x) : #graf 2
    return  -x**2 + 4*x - 5
lst = np.arange(-10, 10, 1E-5) # Liste med masse x verdier som vi bruker for å sjekke.
skjaeringer = [] # Liste med alle skjæringene, y verdiene altså.
x_verdi_som_gir_skjaering = [] # Alle x verdier som gir skjæring.
for x in lst:
    if abs(g(x) - h(x)) <= 1E-4 and abs(g(x) - h(x)) > 0 : # Sjekker når differansen mellom y er minst mulig
        skjaeringer.append(g(x))
        skjaeringer.append(h(x))
        x_verdi_som_gir_skjaering.append(x) # Vil se hvilken x verdi som gir skjæringspunktet. Får mange svar, derfor skal jeg sette alt i i en array og ta første og siste elementet.
                                            # Det er veldig lite forskjell mellom punktene, så jeg bare runder av.
    else:
        continue

forste_skjaering_y = skjaeringer[0] # Tar den første skjæringen, y verdien i skjæringen.
andre_skjaering_y = skjaeringer[-1] #  Tar siste skjæringen, y verdien.

print("Første skjæringspunkt: ({},{})".format(round(x_verdi_som_gir_skjaering[0],3), round(forste_skjaering_y, 2))) #Runder av fordi det er mye desimaler.
print("Andre skjæringspunkt: ({},{})".format(round(x_verdi_som_gir_skjaering[-1],2), round(andre_skjaering_y,2)))  #Runder av fordi det er mye desimaler.

# Dersom du har x^3 på den ene:
# midt_leng_liste_med_x = len(x_verdi_som_gir_skjaering) // 2 
# midt_leng_liste_med_y = len(skjaeringer) // 2
# tredje_skjaering_x = x_verdi_som_gir_skjaering[midt_leng_liste_med_x]
# tredje_skjaering_y = skjaeringer[midt_leng_liste_med_y]
# print("Tredje skjæringspunkt: ({}, {})".format(round(tredje_skjaering_x,3), round(tredje_skjaering_y,3)))