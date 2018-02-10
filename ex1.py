from math import *;

#1: calcule la table de multiplication modulo n
def mult_mod(n):
	liste = [];
	tmplist = [];
	for i in range(0, n):
		for j in range(0, n):
			tmplist.append(i*j%n);	
		liste.append(tmplist);
		tmplist = [];
			
	return liste;

l = mult_mod(6);

def display(liste):
	for l in liste:
		print l;
			
#2: calcul inverse de m modulo n
def inverse(m, n, l):
	m = m%n;
	a = l[m];
	for i in range(n):
		if a[i] == 1:
			return i;
	return 0;

#3: calcule l'ensemble des diviseurs d'un entier n
def diviseurs(n):
	l= [];
	for i in range(1, n+1):
		if n % i == 0:
			l.append(i); 
	return l;


#4 calcule pgcd m et n
def pgcd(m, n):
	lm = diviseurs(m);
	ln = diviseurs(n);
	for i in reversed(lm):
		for j in reversed(ln):
			if i == j:
				return i;
	return 1;
	
#display(diviseurs(28));
print pgcd(50, 24)
#print inverse(5, 6, l);
