import numpy as np
from scipy import optimize as opt

f = np.array([
    10, 8, 6, 9, 18, 20, 15, 17, 15, 16, 13, 17
])

# x11 + x12 + x13 + x14 <= 1000
# x21 + x22 + x23 + x24 <= 600
# x31 + x32 + x33 + x34 <= 500

# 5 * x11 + 7 * x21+ 4 * x31 <= 2880
# 7 * x12 + 12 * x22+ 14 * x32 <= 2880
# 4 * x13 + 8 * x23+ 9 * x33 <= 2880
# 10 * x14 + 15 * x24+ 17 * x34 <= 2880

A = np.array([
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [5, 0, 0, 0, 6, 0, 0, 0, 13, 0, 0, 0],
    [0, 7, 0, 0, 0, 12, 0, 0, 0, 14, 0, 0],
    [0, 0, 4, 0, 0, 0, 8, 0, 0, 0, 9, 0],
    [0, 0, 0, 10, 0, 0, 0, 15, 0, 0, 0, 17]
])
b = np.array([
    [1000, 600, 500, 48 * 60, 48 * 60, 48 * 60, 48 * 60]
])

res = opt.linprog(-f, A, b, method='simplex')

xx = res.x
fun = res.fun
x = np.round(xx)


if x[0] + x[1] + x[2] + x[3] > 1000:
    print("uslov 1")

if x[4] + x[5] + x[6] + x[7] > 600:
    print("uslov 2")

if x[8] + x[9] + x[10] + x[11] > 500:
    print("uslov 3")

# 5 * x11 + 7 * x21+ 4 * x31 <= 2880
# 7 * x12 + 12 * x22+ 14 * x32 <= 2880
# 4 * x13 + 8 * x23+ 9 * x33 <= 2880
# 10 * x14 + 15 * x24+ 17 * x34 <= 2880

if 5 * x[0] + 6 * x[4] + 13 * x[8] > 2880:
    print("uslov 4")

if 7 * x[1] + 12 * x[5] + 14 * x[9] > 2880:
    print("uslov 5")

if 4 * x[2] + 8 * x[6] + 9 * x[10] > 2880:
    print("uslov 6")

if 10 * x[3] + 15 * x[7] + 17 * x[11] > 2880:
    print("uslov 7")

print(x)
print(-fun)