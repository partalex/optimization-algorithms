import random
import copy
import numpy as np
import matplotlib.pyplot as plt

import math as ma

input = np.array(
    [173669, 275487, 1197613, 1549805, 502334, 217684, 1796841, 274708, 631252, 148665, 150254, 4784408, 344759, 440109,
     4198037, 329673, 28602, 144173, 1461469, 187895, 369313, 959307, 1482335, 2772513, 1313997, 254845, 486167,
     2667146, 264004, 297223, 94694, 1757457, 576203, 8577828, 498382, 8478177, 123575, 4062389, 3001419, 196884,
     617991, 421056, 3017627, 131936, 1152730, 2676649, 656678, 4519834, 201919, 56080, 2142553, 326263, 8172117,
     2304253, 4761871, 205387, 6148422, 414559, 2893305, 2158562, 465972, 304078, 1841018, 1915571])


def opt(input, x):
    F1 = 2 ** 25
    F2 = 2 ** 25
    for i in range(64):
        if x[i] == 1:
            F1 = F1 - input[i]
        elif x[i] == 2:
            F2 = F2 - input[i]
        if F1 < 0 or F2 < 0:
            return 2 ** 26
    return F1 + F2


hMax = 13.0


def hi(i):
    return ((1 - hMax) / (100000 - 1)) * (i - 1) + hMax


suma = [0] * 1000000
count = 0
x_glob = np.random.randint(3, size=64)
opt_glob = opt(input, x_glob)

for a_joj in range(5):
    x_min = np.random.randint(3, size=64)
    opt_min = opt(input, x_min)
    niz_crtanje = []
    count = count + 1
    print("a_joj = " + str(a_joj))
    for j in range(10):
        print("j = " + str(j))
        x_old = copy.deepcopy(x_min)
        opt_old = opt_min
        T = 64 * (1024 ** 2)
        for i in range(100000):
            opt_old = opt(input, x_old)  # racunanje stare vr opt
            broj_pozicija = int(np.floor(hi(i)))  # hi mi vrati broj pozicija koje menjam
            pozicije = np.random.randint(63, size=broj_pozicija)
            x_new = copy.deepcopy(x_old)
            for ind in pozicije:
                x_new[ind] = np.random.randint(3)
            opt_new = opt(input, x_new)
            dE = opt_new - opt_old
            if dE < 0:  # tacka na koju skacem i tacka koja mi je glob min
                opt_old = opt_new
                x_old = copy.deepcopy(x_new)
                if opt_new < opt_min:
                    opt_min = opt_new
                    x_min = copy.deepcopy(x_new)
                    # print(opt_min)
            else:  # ako je razlika > 0, tj nova tacka je losija, daje se sansa tacki da se uskoci u nju
                p = ma.exp(-1 * dE / T)
                rand = random.uniform(0, 1)
                if rand <= p:
                    opt_old = opt_new
                    x_old = copy.deepcopy(x_new)
            T = T * 0.95
            niz_crtanje.append(opt_min)
        # print(x_min)
        # print(opt_min)
    plt.loglog(niz_crtanje)
    suma = np.add(suma, niz_crtanje)
    # print(niz_crtanje)
    if opt_min < opt_glob:
        x_glob = copy.deepcopy(x_min)
        opt_glob = opt_min
print(x_glob)
print(opt_glob)

newList = [x / 20 for x in suma]
plt.loglog(newList)

plt.xlabel('Iteration')
plt.ylabel('Optimization function')
plt.grid()
plt.savefig("graphic.png")
plt.show()
