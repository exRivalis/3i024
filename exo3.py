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
       n=ord(i)-65  # i devient n de 0 à 25
       n_chiffre=chiff_cesar_nb(n,cle) # n_chiffre reçois la valeur numerique du chiffrement de la valeur numerique de i
       i_chiffre=chr(n_chiffre+65) # retour au lettres
       text_chiffre+=i_chiffre # concaténation de la chaine chiffré avec le caractere chiffré
       
       
   return text_chiffre
   
def cesar_attaque(text,cle):
        return chiff_cesar(text,-cle)  # appel à cesar_chiffre avec -cle
 
 
      
# Q2
def chiff_monoalphabetique(text,cle):
    text_chiffre=''
    
    for i in text:
        i_chif=ord(i)-65
        text_chiffre+=str(cle[i_chif])
        
    return text_chiffre

def dechiff_monoalphabetique(text_chiffre,cle):
    
    text=''
    
    for i_chif in text_chiffre:
        for elem in range(26):
            if ord[i_chif]==elem:
                text+=elem
    return text
                

#Q3


def chiff_vigenere(text,cle):

    text_chiffre=''
    
    for t in  text:
        t_chiff=chiff_cesar(t,ord(cle[t])-ord(t))
        text_chiffre+=t_chiff
    
    return text_chiffre
    

def dechiff_vigenere(text_chiffre,cle):

    text=''
    
    for t_chiff in text_chiffre:
        t=cesar_attaque(t_chiff,ord(cle[t_chiff])-ord(t_chiff))
        text+=t
    
    return text


#le main
print ("Entrez une phrase a chiffrer : ")


text_a_chiffre=raw_input()
print text_a_chiffre
print("Veuillez entrer une une cle : ")
cle_s = raw_input()
cle = int(cle_s)	

#test cesar
text_chiffre=chiff_cesar(text_a_chiffre,cle)
print ("le chiffrement de cesar pour la phrase ",text_a_chiffre," est la phrase suivante ",text_chiffre)
text_dechiffre=cesar_attaque(text_chiffre,cle)
print text_dechiffre


