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
	# print("p: ", p, " q: ", q)
	n = p*q
	phi = (p-1)*(q-1)

	#e est premier avec (p-1)(q-1)
	e = tools.gen_prime_with(phi, size)
	#d inverse de e modulo(p-1)(q-1)
	d = tools.inverse_mod(e, phi)

	bob_privee = (n, d)
	bob_publique = (n, e)
	# print "bob ", bob_privee, bob_publique
	return bob_privee, bob_publique
	

#chiffrement d'un message m
def chif_rsa(m, b_pub):
	#Alice calcul c = m^e mod n
	e = b_pub[1]
	n = b_pub[0]
	C = 1
	for i in range(e):
		C = (C*m)%n
	# print(m,"^",e,"=",C)
	#c = np.power(m, e) % n
	# print "chiff n: ",n, " e: ",e, " M: ",m," C: ", C
	return C

def dechif_rsa(c, b_priv):
	#Bob dechiffre m = c^d mod n
	n = b_priv[0]
	d = b_priv[1]
	#D = np.power(c, d) % n
	D = 1
	for i in range(d):
		D = (D*c)%n
	# print "dech  n: ", n, " d: ",d," D: ", D
	return D

bob_privee, bob_publique = gen_bob(10)

m = 589
c = chif_rsa(m, bob_publique)
d = dechif_rsa(c, bob_privee)
print ("n: ",bob_publique[0], "M: ", m, " C: ",c," D: ", d)
# chif = np.power(14, 3) % 33
# dehif = np.power(chif, 7) % 33
# C = 5
# print("TEST")
# M = 14
# C = M
# D = 81
# e = 3
# d = 7
# p = 3
# q = 11
# n = p*q
#print("modulo ", e*d % ((q-1)*(p-1)))
# for i in range(d*e-1):
# 	C = (C*C) % n
# print(M, C, D)