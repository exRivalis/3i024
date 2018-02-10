#param par ligne de commande
import sys

#frequence d'apparition caractere dans un fichier
def frequence(file_name):
	text_file = None
	#si le fichier existe on l'ouvre et on continue sinon c'est fini
	try:
		text_file = open(file_name, 'r')
	except IOError:
		print 'entrez un nom de fichier valide'

	alphabet = {}
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

	text_file.close();

	return alphabet




def traitement(read_path, write_path):
	#open file where we write all item of the dictionary who will creat by our fonction
	result = open(write_path,"w")
	f = frequence(read_path)
	for key, value in f.items():
		#print key, value*100
		result.write(key)
		result.write(" %f\n" %(value))
	result.close()

def main(args):
	#get path from command line
	if len(args) != 3:
		print 'usage : python exo2.py read_path write_path'
	else:
		#nouveau fichier
		write_path = args[2]
		#fichier contenant me text a analyser
		read_path = args[1]

		traitement(read_path, write_path)
		return 
#execution main
main(sys.argv)
