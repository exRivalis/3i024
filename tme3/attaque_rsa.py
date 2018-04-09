import tools
import numpy as np

#renvoie les fractions continues de a/b
def fraction(a, b, frac):
    q = int(a/b)
    r = a%b
    frac.append(q)
    if(r>1):
        return fraction(b, r, frac)
    frac.append(b)
    return frac

a = 15625
b = 6842
print(fraction(a, b, []))

#attque de Wiener
#on connait a, e et Phi(n), on cherche d tq ed = 1 [Phi(n)]
