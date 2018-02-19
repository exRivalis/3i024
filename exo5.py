#indice de coincidence d'un texte est la probabilite de tirer deux fois la meme lettre dans le texte
#n : nombre de lettres du texte
#ni : nombre de la i eme lettre de la l'alphabet dans le texte
#P(ni) = 2 parmis ni / 2 parmis n = ni(ni-1)/ n(n-1) -> proba de tirer deux fois la i eme lettre
#IC = somme(P()) entre 1 et 26

import sys

#Q1
def p(x, n):
    res = float(x*(x-1)) / (n*(n-1))
    return res

#calcul indice de coincidence
def IC(text):
    freq = [0 for x in range(26)] #contient nbre apparition de la i eme lettre
    size = len(text) #nombre de lettres dans le text
    #print size
	#calcul nombre d'apparition
    for ch in text:
        if 65 <=ord(ch) < 97:
            #miniscule
            n = ord(ch) - 65
            freq[n] += 1
        elif ord(ch)>=65:
            #majuscule
            n = ord(ch) - 97
            freq[n] += 1


    ic = 0 #indice de coincidence
    #print freq
    for i in freq:
    	#print size
    	ic += p(i, size)
    return ic


#longueur de la cle d'un chiffrement de vigenere
#reperer les motifs qui se repete dans le texte
#mesurer la distance entre deux memes motifs
#calculer le pgcd entre les longueurs trouvees -> Kasiski
def pgcd(a, b):
    while (b > 0):
        r = a%b
        a, b = b, r
    return a
#autrement calculer IC des sous-chaines de longueur k allant de 3 a 24
#reperer les IC qui sortent de l'ordinaire et calculer le pgcd de leur longueurs
def longueur_cle_vigenere(fichier):
	f = open(fichier, 'r')
	text  = ''
	list_ic = []#repertorie les ic selon la longuer de k de la sous-chaine
	#stock le texte dans une chaine de caractere
	for line in f:
		text += line
    #calcul ic
	for k in range(3, 25):
		#pour chauqe val de k on calcul l'IC
		ic = 0
		cpt = 0
		for i in range(0, len(text), k):
            #t contient une chaine de caractere de taille k
			t = text[i:i+k]
			if len(t) > 1:
				ic += IC(t)
				cpt += 1
		list_ic.append((k, float(ic)/cpt))
        #couples longueur de sous-chaine k et l'indice de coincidence correspondant
    list_ic = sorted(list_ic, key=lambda ligne: ligne[1], reverse=True)
    #affichage des (k, ic)
    for l in list_ic:
        print l
    #recup les longuers des n meilleurs scores
    n = 0
    print ("\nnombre de valeurs a recuperer: ")
    n = int(raw_input())

    longueurs_k = []
    for i in range(n):
        longueurs_k.append(list_ic[i][0])

    pg = longueurs_k[0]
    for i in range(1, n, 2):
        pg = pgcd(pg, longueurs_k[i])

    print ("pgcd = ", pg)
#Q3
#cryptanalyse par decalage

def main(args):
    if len(args) != 2:
        print "python exo5.py text_path"
    else:
        cpt = 0 #nombre total de lettres
        freq = [0]*26 # nombre d'apparition de chaque lettre
        text_file = open(args[1], 'r')
        text = ''
        #l'ecrire dans une chaine de caractere
        for line in text_file:
			text += line

        ic = IC(text)
    	text_file.close()

    	#calcul et renvoie ic
    	#print freq
    	return ic

#print main(sys.argv)
longueur_cle_vigenere(sys.argv[1])
