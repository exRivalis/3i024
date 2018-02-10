#cryptanalyse d'un texte en francais
"""
on connait la frequence d'apparition des lettre en francais grace a une analyse de textes 
a partir de la on peut faire des hypotheses sur la clee de codage
sachant qu'on part d'un chiffrement monoalphabetique dans le meme alphabet chaque lettre correspond une autre lettre dans notre meme alphabet
"""

"""
on prend en param le texte a dechiffrer plus le texte qui nous servira de reference pour les frequences
"""
import sys
from frequence import *

if len(sys.argv) != 3:
	print "python exo4.py texte_dechiffrer texte_de_reference"
else:
	file_path_c = sys.argv[1]
	file_path_fr = sys.argv[2]
	
	freq_chif = frequence(file_path_c)
	ref_file = open(file_path_fr, 'r')
	"""
	for key, value in freq_chif.items():
		print key, value
	
	print "freq fr"
	
	"""
	#remplire le dictionnaire avec les valeurs de du fichier de ref
	freq_fr = {}
	for l in ref_file:
		words = l.split()
		print words[0]
		freq_fr[words[0]] = float(words[1])
	
	#trier les deux tableaux par ordre croissant de frequence
	freq_fr = sorted(freq_fr.values())
	freq_chif = sorted(freq_chif.values())
	#print freq_chif
	#print freq_fr
	
	#dictionnaire de dechiffrement
	dict_d = {}
	#dict_d[freq_chif.pop()]
	print freq_fr
