import random
import numpy as np
import matplotlib.pyplot as plt

input = np.array(
    [173669, 275487, 1197613, 1549805, 502334, 217684, 1796841, 274708, 631252, 148665, 150254, 4784408, 344759, 440109,
     4198037, 329673, 28602, 144173, 1461469, 187895, 369313, 959307, 1482335, 2772513, 1313997, 254845, 486167,
     2667146, 264004, 297223, 94694, 1757457, 576203, 8577828, 498382, 8478177, 123575, 4062389, 3001419, 196884,
     617991, 421056, 3017627, 131936, 1152730, 2676649, 656678, 4519834, 201919, 56080, 2142553, 326263, 8172117,
     2304253, 4761871, 205387, 6148422, 414559, 2893305, 2158562, 465972, 304078, 1841018, 1915571])


def opt(x):
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

vrv_1 = 0.8
vrv_2 = 0.15
suma = [0] * 1000000
pokretanje_najbolji = np.random.randint(3, size=64)
for pokretanje in range(0, 20):
    matrica = []
    najbolji = np.random.randint(3, size=64)
    niz_crtanje = []
    for koka in range(0, 20000):
        matrica.append(np.random.randint(3, size=64))

    for broj_generacija in range(0, 50):
        matrica.sort(key=opt)
        # suma = np.add(suma, niz_crtanje)
        if opt(najbolji) > opt(matrica[0]):
            najbolji = matrica[0]
        niz_crtanje.append(opt(najbolji))
        if opt(pokretanje_najbolji) > opt(najbolji):
            pokretanje_najbolji = najbolji

        nova_generacija = []
        broj_parova = 0
        while broj_parova < 20000:
            x = matrica[random.randint(0, 4000)]
            y = matrica[random.randint(0, 4000)]
            random_float = random.uniform(0, 1)
            if random_float < vrv_1:
                poz_preseka = random.randint(0, 64)
                temp = np.concatenate((x[:poz_preseka], y[poz_preseka:]))
                nova_generacija.append(temp)
                broj_parova = broj_parova + 1
            else:
                nova_generacija.append(x)
                nova_generacija.append(y)
                broj_parova = broj_parova + 2

        for koka in nova_generacija:
            random_float = random.uniform(0, 1)
            if random_float < vrv_2:
                rand_pozicija = random.randint(0, 63)
                koka[rand_pozicija] = random.randint(0, 3)
        matrica = nova_generacija

    plt.loglog(niz_crtanje)

    print(najbolji)
    print(opt(najbolji))

# newList = [x / 20 for x in suma]
# plt.loglog(newList)

plt.xlabel('Iteration')
plt.ylabel('Optimization function')
plt.grid()
plt.savefig("graphic.png")
plt.show()
