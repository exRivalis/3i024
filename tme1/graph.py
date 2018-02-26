import sys

if len(sys.argv) != 2:
	print "graph fichier_freq"
else:
	f = open(sys.argv[1], 'r')
	#dessin graph
	
	f.close()
