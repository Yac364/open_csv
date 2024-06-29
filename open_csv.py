import csv

# Ouvrir le fichier CSV en lecture avec un raw string
with open(r'C:\Users\nabil\Downloads\cities.csv', 'r') as fichier:
    lecteur = csv.reader(fichier, delimiter=';')
    for ligne in lecteur:
        print(ligne)
