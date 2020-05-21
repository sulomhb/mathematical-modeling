# cos x = x & sin x = x løsning.
# bare bytt ut math.cos med math.sin eller motsatt.

import math
import numpy as np

n = np.arange(-1, 1, 1E-3, float) # lager en liste med mange små tall
c = [i for i in n if math.sin(i) >= i - 1E-5] # går over alle tallene i lista og sjekker math.cos(x) er minst mulig.
print(round(c[-1], 3)) # printer ut den minste verdien med 3 desimaler.