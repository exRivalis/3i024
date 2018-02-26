#!/usr/bin/python
# -*- coding:UTF-8 -*-

# EXO3

# Q1
def chiff_cesar_nb(nb,cle):
    return (nb+cle)%26

def dechiff_cesar_nb(nb,cle):
    return (nb-cle)%26


def chiff_cesar(text,cle):

   text_chiffre=""

   for i in text:
       # i devient n de 0 à 25
       #Maj / min
       if ord(i) < 97:
           dn = 65
       else:
            dn = 97

       n = ord(i) - dn
       n_chiffre=chiff_cesar_nb(n,cle) # n_chiffre reçois la valeur numerique du chiffrement de la valeur numerique de i
       i_chiffre=chr(n_chiffre+dn) # retour au lettres
       text_chiffre+=i_chiffre # concaténation de la chaine chiffré avec le caractere chiffré



   return text_chiffre

def cesar_attaque(text,cle):
        return chiff_cesar(text,-cle)  # appel à cesar_chiffre avec -cle



# Q2
def chiff_monoalphabetique(text,cle):
    #la cle de codage est un alphabet de la meme taille que l,alphabet d'entree dans notre cas
    #la cle de chifferement est un ensemble de lettre
    text_chiffre=''

    for i in text:
        #Maj / min
        if ord(i) < 97:
            i_chif=ord(i)-65
        else:
            i_chif = ord(i) - 97
        text_chiffre+=str(cle[i_chif])

    return text_chiffre

def dechiff_monoalphabetique(text_chiffre,cle):
    #cle de dechifferement est un ensemble de de lettres (26 dans notre cas)
    #c'est la meme cle utilisee pour chiffrer
    text=''

    for i_chif in text_chiffre:
        #si cest une majuscule ou une miniscule
        if ord(i_chif) < 97:
            dn = 65
        else:
            dn = 97

        for elem in range(26):
            if i_chif == cle[elem]:
                text += str(unichr(elem + dn))

    return text


#Q3
#rend rang (0 - 25) de la lettre qu'elle soit ecrite en majuscule ou non
def rang(c):
	if ord(c)<97:
		#miniscule
		return ord(c) - 65
	#majuscule
	return ord(c) - 97

#Vigenere
def chiff_vigenere(text,cle):

    text_chiffre=''
    cpt = 0
    print cle
    for c in text:
    	#print cle[cpt%len(cle)], rang(cle[cpt%len(cle)])
        cc = chiff_cesar(c, rang(cle[cpt%len(cle)]))
        text_chiffre += cc
        cpt+=1

    return text_chiffre

    """for t in  text:
        t_chiff=chiff_cesar(t,ord(cle[t])-ord(t))
        text_chiffre+=t_chiff

    return text_chiffre"""


def dechiff_vigenere(text_chiffre,cle):

    text=''
    cpt = 0

    for c in text_chiffre:
        cd = cesar_attaque(c, rang(cle[cpt%len(cle)]))
        text += cd
        cpt+=1

    return text
    """for t_chiff in text_chiffre:
        t=cesar_attaque(t_chiff,ord(cle[t_chiff])-ord(t_chiff))
        text+=t

    return text"""

#affichage menu avec choix de la methode a utiliser
def main():
    print ("______MENU______")
    print ("1: chiffrement de Cesar")
    print ("2: dechiffrement de Cesar")
    print ("3: chiffrement de mono-alphabetique")
    print ("4: dechiffrement de mono-alphabetique")
    print ("5: chiffrement de Vigenere")
    print ("6: dechiffrement de Vigenere")

    choix = int(raw_input())

    if choix == 1:
        print ("1: chiffrement de Cesar")
        print ("Entrez texte a chiffrer : ")
        text_a_chiffre=raw_input()
        print ("Veuillez entrer une cle: ")
        cle = int(raw_input())
        text_chiffre = chiff_cesar(text_a_chiffre, cle)
        print ("Texte chifre",text_chiffre)

    elif choix == 2:
        print ("2: dechiffrement de Cesar")

        print ("Entrez texte a dechiffrer : ")
        text_chiffre=raw_input()
        print ("Veuillez entrer une cle: ")
        cle = int(raw_input())
        text_dechiffre = cesar_attaque(text_chiffre, cle)
        print ("Texte dechiffree ",text_dechiffre)

    elif choix == 3:
        print ("3: chiffrement de mono-alphabetique")

        print ("Entrez texte a chiffrer : ")
        text_a_chiffre=raw_input()
        print ("Veuillez entrer une cle: ")
        cle = raw_input()
        text_chiffre = chiff_monoalphabetique(text_a_chiffre, cle)
        print ("Texte chifre",text_chiffre)

    elif choix == 4:
        print ("4: dechiffrement de mono-alphabetique")

        print ("Entrez texte a dechiffrer : ")
        text_chiffre=raw_input()
        print ("Veuillez entrer une cle: ")
        cle = raw_input()
        text_dechiffre = dechiff_monoalphabetique(text_chiffre, cle)
        print ("Texte dechiffree ",text_dechiffre)

    elif choix == 5:
        print ("5: chiffrement de Vigenere")

        print ("Entrez texte a chiffrer : ")
        text_a_chiffre=raw_input()
        print ("Veuillez entrer la cle: ")

      	#recup cle
        cle = raw_input();

        text_chiffre = chiff_vigenere(text_a_chiffre, cle)
        print ("Texte chifre",text_chiffre)

    elif choix == 6:
        print ("6: dechiffrement de Vigenere")

        print ("Entrez texte a dechiffrer : ")
        text_chiffre=raw_input()
        print ("Veuillez entrer la cle: ")
        #recup cle
        cle = raw_input()

        text_dechiffre = dechiff_vigenere(text_chiffre, cle)
        print ("Texte dechiffree ",text_dechiffre)


main()
