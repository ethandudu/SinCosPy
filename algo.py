# Importation des librairies
from math import *
from colorama import *
import time

print(Fore.CYAN, "Bienvenue dans le calculateur de Sinus/Cosinus")  # phrase de bienvenue
print(Fore.WHITE)

# Définitions des variables
a = int(input("Merci d'entrer a : "))  # définition de a
b = int(input("Merci d'entrer b : "))  # définition de b
print()
print(Fore.LIGHTGREEN_EX, "Calcul : a*pi/b")  # on montre le calcul

# Calcul
cosinus = cos(a * pi / b)  # on calcule le cosinus
sinus = sin(a * pi / b)  # on calcule le sinus

# On met de la poudre de perlinpinpin
print(Fore.MAGENTA)
print("Calcul en cours, veuillez patienter 0%")
time.sleep(0.5)
print("calcul en cours, veuillez patienter . 33%")
time.sleep(0.5)
print("Calcul en cours, veuillez patienter .. 66%")
time.sleep(0.5)
print("Calcul en cours, veuillez patienter ... 99%")
time.sleep(0.5)
print("Calcul terminé 100%")

# Résultats
print()
print(Fore.CYAN, "Résultats :")
print(Fore.LIGHTRED_EX, "cos= ", cosinus)  # on affiche le cosinus en rouge clair
print(Fore.LIGHTRED_EX, "sin= ", sinus)  # on affiche le sinus en rouge clair

print(Fore.LIGHTBLUE_EX, "TIPS = V3/2=0.866 et V2/2=0.707")  # on affiche un équivalent
exit()
