import random
import math as m
from suma import suma
import numpy as np

n = 5;
B = 20 * m.pi
Q = m.pi / 4
d = 1 / 20
f = B * d * m.cos(Q)

# index = 0;
x1 = random.uniform(3.5, 4.5)
x3 = random.uniform(3.5, 4.5)

if x1 > x3:
    t = x1
    x1 = x3
    x3 = t

while (True):
    # fTacno = -abs(suma(f, n, step))

    x2 = (x1 + x3) / 2

    f1 = -abs(suma(f, 5, x1))
    f2 = -abs(suma(f, 5, x2))
    f3 = -abs(suma(f, 5, x3))

    matrix = np.array([
        [x1 ** 2, x1, 1],
        [x2 ** 2, x2, 1],
        [x3 ** 2, x3, 1]
    ])

    foo = np.array([
        [f1],
        [f2],
        [f3]
    ])

    inverted = np.linalg.inv(matrix)

    res = np.dot(inverted, foo)

    xmin = -1 * res[1][0] / (2 * res[0][0])

    fnew = -abs(suma(f, 5, xmin))

    niz = [
        (x1, f1),
        (x2, f2),
        (x3, f3),
        (xmin, fnew)
    ]

    sorter = lambda x: (x[1], x[0])
    sorted_l = sorted(niz, key=sorter)
    print(niz)

    break

    index = index + 1
    step = step + 0.01

# for i in niz_suma:
# print(i)
