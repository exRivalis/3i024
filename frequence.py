
def frequence(fichier):
	text_file = None
	#si le fichier existe on l'ouvre et on continue sinon c'est fini
	try:
		text_file = open(fichier, 'r')

		alphabet = {'A':0}
		cpt = 0

		for line in text_file:
			for ch in line:
				#if ch != ' ' and ch != '\n':
				cpt+=1
				if not (ch in alphabet):
					alphabet.update({ch: 1})
				else :
					alphabet[ch] += 1

		for key, value in alphabet.items():
			alphabet[key] = float(value)/cpt
			#write in file all item of dictionary

		text_file.close()
		return alphabet

	except IOError:
		print 'entrez un nom de fichier valide'
