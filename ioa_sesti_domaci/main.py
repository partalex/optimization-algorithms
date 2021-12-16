from builtins import print

import np as np
import numpy

import parameters

from scipy import optimize as opt

# optimize.linprog(method='simplex')
# 48 casovA * 60 min


# r1 = 5 min/serv
# p1 = 10 din/serv

matrica_nejednacine = np.array() [
    [],
])
res = opt.linprog(parameters.price, matrica_nejednacine)
