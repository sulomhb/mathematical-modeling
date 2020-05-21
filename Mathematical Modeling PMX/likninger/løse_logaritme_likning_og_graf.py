import numpy as np
import matplotlib.pyplot as plt

def a(x):
    return 2**x #graf 1
def b(x):      # graf 1 = graf 2
    return x + 2 #graf 2

arr = np.arange(-3,3, 1E-5) # Ha riktig intervall.
for x in arr:
    if a(x) - b(x) <= 1E-5 and a(x) - b(x) > 0: # Bytt litt på 1E-5 dersom du ikke får svar.
        print("x = {}".format(round(x,3))) # Pass på avrundingen.
    else:
        continue

plt.plot(arr, a(arr))
plt.plot(arr, b(arr))
plt.show()