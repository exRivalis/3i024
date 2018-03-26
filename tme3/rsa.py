import tools
import numpy as np
#chiffrement RSA:
#	Bob genere p, q, e et d
#	p et q deux grand premiers distincts
#	e est premier avec (p-1)(q-1)
#	d inverse de e modulo(p-1)(q-1) -> euclide

#	cle publique de Bob (n, e)
#	cle privee (n, d)

size = 1000 #ordre de grandeur des nombres premiers a generer


def gen_bob(size):
	#p et q deux grand premiers distincts
	p = tools.prime_gen(size)
	q = p
	while(q == p):
		q = tools.prime_gen(size)

	n = p*q
	phi = (p-1)*(q-1)

	#e est premier avec (p-1)(q-1)
	e = tools.gen_prime_with(phi, size)
	#d inverse de e modulo(p-1)(q-1)
	d = tools.inverse_mod(e, phi)

	bob_privee = (n, d)
	bob_publique = (n, e)
	print "bob ", e, d
	return bob_privee, bob_publique
	

#chiffrement d'un message m
def chif_rsa(m, b_pub):
	#Alice calcul c = m^e mod n
	e = b_pub[1]
	n = b_pub[0]
	c = np.power(m, e) % n
	print "chiff ", n, e, c
	return c

def dechif_rsa(c, b_priv):
	n = b_priv[0]
	d = b_priv[1]
	D = np.power(c, d) % n
	print "dech ", n, d, D
	return D

bob_privee, bob_publique = gen_bob(10)

m = 487
c = chif_rsa(m, bob_publique)
d = dechif_rsa(c, bob_privee)
print m, c, d
