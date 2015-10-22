# wisielec, szubienica
# komputer losowo wybera slowo, 
# a gracz probuje odgadnac jego poszczegolne litery
# jesli gracz w pore nie odgadnie slowa maly ludzi zostanie powieszony 


# spersonalizowane przywitanie
name = raw_input("\tCzesc. Jak masz na imie?  ")
name = str(name)

print "\n\tCzesc ", name
#print "\n\tZasady gry: Komputer wybiera ukryte slowo, a zadaniem gracza jest proba jego stopniowego odgadniecia,"
#print "\n\tlitera po literze. Za kazdym razem, gdy litera podana przez gracza jest niepoprawna,"
#print "\n\tkomputer pokazuje nowy rysunek wieszanej postaci." 
#print "\n\tJesli gracz nie odgadnie slowa w pore, ludzik z rysunku traci zycie."
#print "\n\tNIE UZYWAMY ZNAKOW DIAKRYTYCZNYCH"
print ("\n\tZaczynamy gre wisielec! Powodzenia!!")



# STALE - rysunek szubienicy
HANGMAN = (

"""
	______________
	|	    |
	|	    
	|	  
	|	 
	|	   
	|	   
	|	   
	|
--------------
""", 
"""
	______________
	|	    |
	|	    O
	|	   
	|	    
	|	    
	|	   
	|	   
	|
--------------
""",
"""
	______________
	|	    |
	|	    O
	|	   -+-
	|	    
	|	    
	|	   
	|	   
	|
--------------
""",
"""
	______________
	|	    |
	|	    O
	|	  /-+-
	|	 /    
	|	    
	|	   
	|	   
	|
--------------
""",
"""
	______________
	|	    |
	|	    O
	|	  /-+-\\
	|	 /     \\
	|	    
	|	   
	|	   
	|
--------------
""", 
"""
	______________
	|	    |
	|	    O
	|	  /-+-\\
	|	 /  |  \\
	|	    |
	|	   
	|	   
	|
--------------
""",
"""
	______________
	|	    |
	|	    O
	|	  /-+-\\
	|	 /  |  \\
	|	    |
	|	   | 
	|	   | 
	|
--------------
""",
"""
	______________
	|	    |
	|	    O
	|	  /-+-\\
	|	 /  |  \\
	|	    |
	|	   | |
	|	   | |
	|
--------------
"""
)

# okreslenie ilosci blednych odpowiedzi - zalezy od ilosic rysunkow. Pierwszy rusunek jest od razu stad "-1"
MAX_WRONG = len(HANGMAN) -1
#print "ilosc nieudanych prob to:", len(HANGMAN)

# przykladowy pakiet slow do wylosowania
# wazne by zwrocic uwage na wielkosc liter funkcja lower, upper, nie wuzywam znakow diakrytycznych
WORDS = ("python", "helikopter", "traktor", "skomplikowany", "ksylofon")

# wybierz losowo jedno ze slow z pakietu WORDS
import random
word = random.choice(WORDS)

# w celu testow programu mozna ujawnic zgadywane slowo
print "wylosowane slowo to: ", word

#ile liter ma wybrane slowo
print "\n\n Wyraz, ktory masz odgadnac ma dlugosc:", len(word)

#jak wyglada odgadywane slowo, " _ " oznacza miejsce na wipsanie litery
so_far = "*" * len(word)
print "\nobecnie zagadka wyglada tak:", so_far

# Licznik - liczba bledow gracza - liczba nietrafione litery
wrong = 0

#litery ktore juz wpisales  nie wystepuja w wyrazie
#is_not = []
#print "litery ktore probowales i nie ma ich w wyrazie", is_not


#zestaw wykorzystanych liter
used = []




while wrong < MAX_WRONG and so_far != word:
	print "\nZgadywane slowo wyglada tak:\n", so_far
	print (HANGMAN [wrong])
	print "pozostalo ci", MAX_WRONG - wrong, "zgadywan zanim komputer cie powiesi"
	#gracz wybiera litere, ktora jego zdaniem moze wystepowac w zgadywanym slowie
	choice = raw_input("\t\tWpisz litere:  ")
	choice = choice.lower()

	while choice in used:
		print "juz wykorzystales litere", choice
		choice = raw_input("\t\tWpisz nowa litere:  ")
		choice = choice.lower()
	used.append(choice)
	
	print "\nWykorzystales juz nastepujace litery:\n", used

	if choice in word:
		print "\tbrawo", choice, "wystepuje w zgadywanym wyrazie !" 
		#aktualizacja zgadywanego slowa - zgadywane slowo obecnie wyglada tak 
		new = ""
		for i in range(len(word)):
			if choice == word[i]:
				new = new + choice   # to samo co new += choise
			else:
				new = new + so_far[i]
		so_far = new

	else:
		print "\tniestety litera", choice, "nie wystepuje w zgadywanym wyrazie"
		wrong = wrong + 1   # to samo co wrong += 1

# zakonczenie gry 
if wrong == MAX_WRONG:
	print(HANGMAN[wrong])
	print "\n zotales powieszony !!!!"
else:
	print "\n Odgadles !!"
	print "\n Zagadkowe slowo to: ", word


raw_input("\n\nAby zakonczyc gre, nacisnij klawisz Enter")