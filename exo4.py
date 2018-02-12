#cryptanalyse d'un texte en francais
"""
on connait la frequence d'apparition des lettre en francais grace a une analyse de textes
a partir de la on peut faire des hypotheses sur la cle de codage
sachant qu'on part d'un chiffrement monoalphabetique dans le meme
alphabet chaque lettre correspond une autre dans l'alphabet
"""

"""
on prend en param le texte a dechiffrer plus le texte
qui nous servira de reference pour les frequences
"""
import sys
from frequence import *
from operator import itemgetter

if len(sys.argv) != 3:
	print "python exo4.py texte_chiffrer freq_texte_de_reference"
else:
	file_path_chif = sys.argv[1]
	file_path_freq = sys.argv[2]


	#recup dico des freq des lettres dans le texte a dechiffrer
	freq_chif = frequence(file_path_chif)
	chif_file = open(file_path_chif, 'r')
	ref_file = open(file_path_freq, 'r')
	"""
	for key, value in freq_chif.items():
		print key, value

	print "freq fr"

	"""


	#remplire dico (lettre, freq) a partir des frequences du texte de reference
	
	freq_fr = {}
	for l in ref_file:
		words = l.split()
		#print words[0]
		freq_fr[words[0]] = float(words[1])


	#trier les deux tableaux par ordre decroissant des frequences
	#pour ce faire les transformer en liste de tuples, pas de tri sur des dictionnaires

	t_freq_fr = []
	t_freq_chif = []

	for key, value in freq_fr.items():
		t_freq_fr.append((key, value))

	for key, value in freq_chif.items():
		t_freq_chif.append((key, value))

	#tri des listes selon le deuxieme element (freq)
	t_freq_chif.sort(key=itemgetter(1), reverse=True)
	t_freq_fr.sort(key=itemgetter(1), reverse=True)
	#trier les deux dicts selon key ()

	dict_d = {}
	#dictionnaire de dechiffrement
	for i in range(len(freq_chif)):
		dict_d[t_freq_chif[i][0]] = t_freq_fr[i][0]

	#dechiffrement
	text = ''
	for line in chif_file:
		for c in line:
			text += dict_d[c]
	print text
