import matplotlib.pyplot as plt
import numpy as np
from main import B
from main import d
from main import n
from main import Q
from suma import suma
import math as m

domen = np.arange(0, 2 * m.pi, 2 * m.pi / 100)

niz_suma = [0] * domen.size
for ind_dt, dt in enumerate(domen):
    f = B * d * m.cos(Q)
    niz_suma[ind_dt] = abs(suma(f, n, dt))

plt.figure()
plt.plot(domen, niz_suma)
plt.show()
