from math import e


def suma(f, n, dt):
    ret_suma = 0 + 0j
    f = f + dt;
    for k in range(0, n):
        ret_suma = complex(ret_suma + e ** (-1j * k * f))
    return ret_suma