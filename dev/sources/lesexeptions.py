fichier = input('Entre un chemin de fichier a ouvrir : ')

try:
    with open (fichier, 'r') as f:
        contenu = f.read()
    print(contenu)

except:
    print('fichier invalide !')

else:
    f.close()