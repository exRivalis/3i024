import math
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
def invers_mod(a, p):
	#renvoie l'inverse modulaire de a par rapport p
	r, u, v = bezout(a, p)
	return u%p
	
def BSGS(n, p, g):
	#n : g^k = n
	#p ordre du groupe cyclique
	#generateur du groupe
	s = int(math.sqrt(p)) + 1 # 
	BS = [] #babystep g^r avce 0<= r <= s-1
	GS = [] #babystep n((g^-s)^q) avce 0<= q <= s-1
	
	for r in range(s):
		BS.append(pow(g, r, p))
	
	u = invers_mod(pow(g, s, p), p)
	
	for q in range(s):
		GS.append(n*pow(u, q, p)%p)
		
	#print GS
	#print BS
	for i in range(len(BS)):
		for j in range(len(GS)):
			if BS[i] == GS[j]:
				#print i
				break;
	#print (i, j)
	k = j*s + i
	return k

print BSGS(3, 23, 11)
