import math
import random
import numpy as np
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

def pgcd(a, b):
	r, u, v = bezout(a, b)
	return (a*u + b*v) 

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



#generer un nombre premier de l'orde de n
def prime_gen(n):
	r = 2
	while(not is_prime(r)):
		r = random.randint(n, n*n)
	return r		

#genere un nombre premier avec p de l'orde de n
def gen_prime_with(p, n):
	x = prime_gen(n)
	
	while(not primes(x, p)):
		x = prime_gen(n)
	return x
	
#verifie si un nombre est premier de facon naive
def is_prime(p):
	sqrt = int(np.sqrt(p))
	#print sqrt
	if p%2 == 0:
		return False
	for i in range(2, sqrt+1):
		if (p%i) == 0:
			return False
	return True

#verifie si deux nombres sont premier entre eux
def primes(a, b):
	return (pgcd(a, b) == 1)
