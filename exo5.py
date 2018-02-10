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
def IC(freq, tot):
    #freq[i] contient nbre apparition de la i eme lettre

    ic = 0 #indice de coincidence

    for i in freq:
        ic += p(i, tot)

        return ic

def main(args):
    if len(args) != 2:
        print "python exo5.py text_path"
    else:
        cpt = 0 #nombre total de lettres
        freq = [0]*26 # nombre d'apparition de chaque lettre
        text_file = open(args[1], 'r')

        #calcul nombre d'apparition
        for line in text_file:
            for ch in line:
                cpt+=1
                if ord(ch) < 97:
                    #miniscule
                    n = ord(ch) - 65
                else:
                    #majuscule
                    n = ord(ch) - 97
                freq[n] += 1

    text_file.close()

    #calcul et renvoie ic
    print freq
    return IC(freq, cpt)

print main(sys.argv)
