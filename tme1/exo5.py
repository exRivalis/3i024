#indice de coincidence d'un texte est la probabilite de tirer deux fois la meme lettre dans le texte
#n : nombre de lettres du texte
#ni : nombre de la i eme lettre de la l'alphabet dans le texte
#P(ni) = 2 parmis ni / 2 parmis n = ni(ni-1)/ n(n-1) -> proba de tirer deux fois la i eme lettre
#IC = somme(P()) entre 1 et 26
import math
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
def kasiski(fichier):
    f = open(fichier, 'r')
    text  = ''
    list_ic = []#repertorie les ic selon la longuer de k de la sous-chaine
    #stock le texte dans une chaine de caractere
    for line in f:
        text += line
    #calcul ic
    for k in range(3, 20):
        #pour chauqe val de k on calcul l'IC
        ic = 0
        cpt = 0
        tmp_str = ''
        for i in range(0, len(text), k):
            #on recup la i eme lettre, par pas de k
            tmp_str = tmp_str + text[i]
        list_ic.append((k, IC(tmp_str)))
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
    print("\npgcd entre: \n"+str(pg))
    for i in range(1, n):
		print longueurs_k[i]
		pg = pgcd(pg, longueurs_k[i])

    print ("\nresultat = " + str(pg))

    """
    maintenant qu'on a la longueur de la cle
    on fait une cryptanalyse par decalage
    pour chaque sous-chaine on appel cesar pour trouver la lettre de codage
    on fait ca pour chaque sous-chaine -> on determine la cle de codage
    """
#Q3
#dechiffrement cesar prend une lettre chiffree et renvoie la lettre en claire
def dechiff_cesar(lettre,cle):
	l =ord(lettre)
	c =ord(cle)
	return chr((l - c)%26+65)
#cryptanalyse par decalage
#diviser le texte entrant en n textes
#textes[i] contient les lettres aux indices i + kn tant que kn < len(texte)
#comtabiliser la frequence des lettres dans chacun des n textes: la plus frequente est souvent E
#effectuer un decalage
def dechiff_vigenere(texte, n):
	liste_textes = []#contient n textes
	for i in range(n):
		liste_textes.append([])
    #recup n textes
	# for i in range(n):
	# 	for k in range(len(texte)):
	# 		if i+k*n < len(texte):
	# 			liste_textes[i].append(texte[i+k*n])
	# 		else:
	# 			continue
	for i in range(len(texte)):
		liste_textes[i%n].append(texte[i])
		# print liste_textes[i%n][-1], texte[i]
	#comptabiliser les occurences
	# print liste_textes[5][5:10]
	# print liste_textes[8][5:10]
	liste_occurence = [] #continet les uplets correspondants aux sous textes (lettre, occurrence)
	for i in range(n):
		lettres_occ = []
		#suppression doublons
		t = liste_textes[i]
		# print liste_textes[i][5:10], i
		lettres = list(set(t))
		# print i
		for j in range(len(lettres)):
			#compter occurrences
			cpt_lettre = 0
			for l in t:
				if l == lettres[j]:
					cpt_lettre +=1
			lettres_occ.append((lettres[j], cpt_lettre)) #contient (lettre, occurrences)

		#lettres est une liste de tuples maintenant
		liste_occurence.append(lettres_occ)

	#liste_occurence contient la liste (lettres, occ) pour chaque sous texte
	# print "liste occurrences: ", liste_occurence
	# determination de la cle de chiffrement
	cle = []
	for text_i in liste_occurence:
		#tri decroissant des occurrences
		text_i = sorted(text_i, key=lambda data: data[1], reverse=True)
		#la premiere est surrement E (en francais en tout cas)
		x = text_i[0][0]
		if 65 <=ord(x) < 97:
			cle.append(chr(((ord(x) - ord('E'))%26 + ord('A')))) # %26 pour rester l'alphabet A-Z
		elif ord(x)>=65: #miniscule
			cle.append(chr(((ord(x) - ord('e'))%26 + ord('a'))))


	#decriptage texte
	texte_claire = ''
	key = ''
	for c in cle:
		key+=c
	print "\nLa cle de chiffrement: " + key
	for i in range(len(texte)):
		texte_claire += (dechiff_cesar(texte[i], cle[i%n]))
	#renvoyer le texte claire
	return texte_claire



#main contenant tout les appels aux autres fonctions
def main(args):
    if len(args) != 2:
        print "python exo5.py text_path"
    else:
        #cpt = 0 #nombre total de lettres
		#freq = [0]*26 # nombre d'apparition de chaque lettre
		#ouverture fichier
		text_file = open(args[1], 'r')
		text = ''
		#l'ecrire dans une chaine de caractere
		for line in text_file:
			text += line
			#fermeture fichier
		text_file.close()
		#ic = IC(text)
		#calcul longueur cle
		kasiski(args[1])
		#demander choix de cle user et faire tant qu'il veut
		choix = 1
		while choix == 1:#on recommence
			l_cle = 0
			print ("\nlongueur de cle de dechiffrement: ")
			l_cle = int(raw_input())

			print("Le message clair:\n" + str(dechiff_vigenere(text, l_cle)))
			#quitter ou essayer une autre longueur
			print ("\nrecommencer (1), quitter (0): ")
			choix = int(raw_input())

		#sortir


main(sys.argv)
# decalage_vigenere("aeeeaeeeaeeeaeeeaeeeaeeeaeeea", 4)
