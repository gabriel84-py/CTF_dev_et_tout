#cahll pas terminé...

import re
import socket
import math
import base64
import codecs
import zlib
import time

# Connexion à la socket TCP
host = 'challenge01.root-me.org'
port = 52022

# Création de la socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# Recevoir les données envoyées par le serveur
data = s.recv(1024).decode()  # Récupérer les données envoyées
print(f"Reçu brut : {data}")

i = 1

while i < 20:
    print('ok')

    #data = s.recv(1024).decode()  # Récupérer les données envoyées
    print(f"Reçu brut : {data}")
    # Utiliser une expression régulière pour extraire la chaîne entre apostrophes
    match = re.search(r"'(.*?)'", data)  # Cherche une chaîne entre apostrophes

    base64_string = match.group(1)  # Récupère la chaîne trouvée

    # Ajouter le padding nécessaire pour le décodage Base64
    padding_needed = 4 - (len(base64_string) % 4)
    if padding_needed < 4:
        base64_string += '=' * padding_needed  # Ajouter le padding

    # Décoder la chaîne Base64
    compressed_data = base64.b64decode(base64_string)  # Décodage de la chaîne Base64
    # Décompresser la chaîne
    decompressed_data = zlib.decompress(compressed_data)
    print("Chaîne décompressée :", decompressed_data.decode('utf-8'))

    # Envoyer la réponse au serveur
    s.sendall(decompressed_data + b'\n')  # Envoyer la chaîne décompressée
    s.sendall(data.encode())

            
    response = s.recv(1024).decode()
    print(f"Réponse du serveur : {response}")


    i += 1

# Fermer la connexion
s.close()