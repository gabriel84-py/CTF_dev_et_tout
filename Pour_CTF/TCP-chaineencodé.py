import re
import socket
import math
import base64

# Connexion à la socket TCP
host = 'challenge01.root-me.org'
port = 52023

# Création de la socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# Recevoir les données envoyées par le serveur (par exemple, le calcul)
data = s.recv(1024).decode()  # Récupérer les données envoyées

print(f"Reçu : {data}")

# Utiliser une expression régulière pour extraire la chaîne entre apostrophes
match = re.search(r"'(.*?)'", data)  # Cherche une chaîne entre apostrophes
if match:
    base64_string = match.group(1)  # Récupère la chaîne trouvée
    # Décoder la chaîne Base64
    decoded_string = base64.b64decode(base64_string).decode('utf-8')
    print("Chaîne décodée :", decoded_string)
else:
    print("Aucune chaîne Base64 trouvée dans les données.")

# Envoyer la réponse au serveur
s.sendall(f"{(decoded_string)}\n".encode())

# Recevoir la réponse du serveur (si nécessaire)
response = s.recv(1024).decode()
print(f"Réponse du serveur : {response}")

# Fermer la connexion
s.close()