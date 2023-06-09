from Poker import Carte
from Poker import Cartes
from Poker import Jeu
from Poker import Main
from Poker import Carre
from Poker import Quinte

print("------------------ Exercice 1 ------------------")
Il s’agit de créer des classes pour modéliser une partie de pocker.
print(Carte())                      # -> Valet de Trèfle (par exemple)
print(Carte())                      # -> Dame de Coeur (par exemple)
print(Carte())                      # -> 8 de Carreau (par exemple)
carte1 = Carte(7,"Coeur")
print(carte1)                       # -> 7 de Coeur
carte2 = Carte("Valet","pic")       # -> ValueError: pic: couleur incorrecte
carte3 = Carte("Valet","Pique")
print(carte3)                       # -> Valet de Pique
##################################################################################################
print("------------------ Exercice 2 ------------------")
# 3 cartes
carte1 = Carte("As","Trèfle")
carte2 = Carte(7,"Coeur")
carte3 = Carte("Valet","Pique")

# un ensemble de cartes (vide au départ)
des_cartes = Cartes()

# on y ajoute les 3 cartes
for une_carte in [carte1,carte2,carte3]:
  des_cartes.ajoute(une_carte)

print(f"{des_cartes=}")

# on le clone
les_memes = Cartes(des_cartes)
print(f"{les_memes=}")

# on pioche dedans tant que l'on peut
try:
  while True:
    print(f"{des_cartes.pioche()=}")
    print(f"{des_cartes=}")
    print(f"{les_memes=}")
except ValueError as e:
  # traceback.print_exc(file=sys.stdout)
  print(e)
print("fin de programme")

##################################################################################################
print("------------------ Exercice 3 ------------------")
un_jeu = Jeu()
print(f"{un_jeu=}")
un_jeu -= Carte('Valet','Coeur')
un_jeu -= Carte('As','Pique')
un_jeu -= Carte(10,'Trèfle')
print(f"{un_jeu=})
      
##################################################################################################
print("------------------ Exercice 4 ------------------")
le_jeu = Jeu()

# on crée 2 mains vides
ma_main = Main(le_jeu)
ta_main = Main(le_jeu)
print(f"{ma_main=}")
print(f"{ta_main=}")

# on y ajoute 3 cartes
for i in range(3):
  ma_main.complete()
  print(f"{ma_main=}")
  ta_main.complete()
  print(f"{ta_main=}")
print(f"{le_jeu=}")

# on tente d'ajouter 25 cartes à la première
try:
  for i in range(25):
    ma_main.complete()
except ValueError as e:
  print(e)

# on tente dajouter 25 cartes à la seconde
try:
  for i in range(25):
    ta_main.complete()
except ValueError as e:
  # traceback.print_exc(file=sys.stdout)
  print(e)

print("fin de programme")
      
##################################################################################################
      
print("------------------ Exercice 5 ------------------")
le_jeu = Jeu()

# une main de 25 cartes
une_main = Main(le_jeu)
for i in range(25):
  une_main.complete()
print(f"{une_main=}")

# recheche tous les carrés contenus dans la main
while True:
  try:
    un_carre = Carre(une_main)               # essai de créer un carré
    # si on est là, c'est qu'un carré a été créé
    print(f"{un_carre=}, {une_main=}")
    une_main -= un_carre                     # on l'enlève de la main
  except RuntimeError as e:
    # si on est là, c'est qu'un carré n'a pas pu être créé
    print(e)
    break

print("fin de programme")
