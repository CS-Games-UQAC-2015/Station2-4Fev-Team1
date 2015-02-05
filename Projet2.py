#Salut mon cher ami. Lis le but de leur jeu.
#Bravo, c'est fait ! Maintenant, nous devons dire a Omar s'il est possible de changer une mot en un autre
#en faisant des tests. Pour te faire sauver du temps va regarder le sample.
#"5" veut dire on va faire 5 tests(un tests contient plusieurs mots)
#"2" veut dire mon test#1 a 2 strings.
# Ensuite on a les deux mots. Et ainsi de suites...
#En output on doit pouvoir dire Case#x:y où x = numéro de cas et y= nombre d'opération a faire ou Fegla won


#ALGORITHME: commencer par identifier les Fegla won (impossible de faire le move)
# Pour ce, s'il existe des lettres qui existe dans un seul mot, Fegla won
# Vérifier que les lettres apparaissent dans le même ordre sans compter leur répétitions

#Sinon, c'est possible.
#1:BOUCLE FOR Comparer les premières lettres de chaque mots. Si elles sont égales, passer à une autre lettre
#2:     Sinon, identifier l'apparition la plus fréquente d'une lettre dans chaque mots, -------------------------------------------------------------------------------< do dat
#3:     Vérifier celles qui n'ont pas cette lettre (ce seront les mots ayant besoin de modifs)
#4:     Vérifier la lettre d'avant de ces mots. Si elles sont les mêmes que la lettre majoritaire, utiliser la règle un (inserer cette lettre)
#5:     Sinon,s'assurer que la lettre est identique à la lettre d'avant utiliser la règle deux (retire cette lettre et décaler vers la gauche)
#5(suite):      TANT QUE l'on obtient pas la bonne lettre

#ATTENTION : Se garder une variable nombre de règle qui commence à 0 et incrémente chaque fois que l'on utilise une règle.
#signé Johnny (tour 1) <-wow, doge!

#FRAME

###################################################################
## Initialisation des variables
###################################################################
T = 0 #number of tests
N = 0 #number of strings to test

###################################################################
##  Prendre les inputs
###################################################################
with open("A-small-practice.in", "r+") as file:
	T = int(file.readline())
	
	###################################################################
	## Mémoriser les mots de chaques tests
	###################################################################
	for i in range (1, T): #Do all cases
		N = int(file.readline())
		strings = []
		
		for j in range (0, N): #Get all strings
			strings.append(file.readline())
	
		###################################################################
		##  Utiliser l'algo (compare strings)
		###################################################################
		#Auto Fegla Won
		#if(len(strings[0]) != len(strings[1])):
		
		#Compare letters, if they're the same, leave as is
		for letter0 in strings[0]:
			for letter1 in strings[1]:
				if letter0 == letter1:
					print("next")

###################################################################
##  Output
###################################################################
x = 1
y = 0
print("Case #" + str(x) + ": " + str(y))
