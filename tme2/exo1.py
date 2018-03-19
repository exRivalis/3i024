import math
#bezout
def bezout(a, b):
	u = 1
	v = 0
	ubis = 0
	vbis = 1
	r = a
	rbis = b
	q = 0
	
	while(rbis != 0):
		q = r/rbis
		(r, u, v, rbis, ubis, vbis) = (rbis, ubis, vbis, r-q*rbis, u-q*ubis, v-q*vbis)
	return r, u, v

print bezout(1221, 876)

#inverse modulaire
def inverse_mod(a, p):
	#renvoie l'inverse modulaire de a par rapport p
	r, u, v = bezout(a, p)
	return u%p


def inverses_anneau(n):
	A = []
	for a in range(n):
		#for b in range(a, n):
		inv_a = (inverse_mod(a, n))
		if inv_a > 0 and inv_a < n and inv_a != a:
			A.append(inv_a)
	return list(set(A))

print inverses_anneau(15)
