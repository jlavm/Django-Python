print "Hola Mundo"

def fight(fighters,mode="boxing"):

	print "Lucha en modo", mode
	for fighter in fighters:
		if(fighter=="Chuck Norris"):
			print "Ha ganado", fighter
	print "Chuck no esta"



fight(["Goku","Bruce Lee","Doraemon"],"kung Fu")