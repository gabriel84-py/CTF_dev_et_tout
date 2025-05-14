import re
import socket
import math

# Connexion à la socket TCP
host = 'challenge01.root-me.org'
port = 52002

# Création de la socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# Recevoir les données envoyées par le serveur (par exemple, le calcul)
data = s.recv(1024).decode()  # Récupérer les données envoyées

print(f"Reçu : {data}")

nombres = re.findall(r'\d+', data)  # Cherche tous les groupes de chiffres
print(nombres)
a, b = map(int, nombres[1:])  # Utiliser seulement les deux derniers éléments

print("a =", a)
print("b =", b)


# Calcul de la racine carrée de n1
sqrt_n1 = math.sqrt(a)

# Multiplier par n2
result = sqrt_n1 * b

# Arrondir à deux décimales
final_result = round(result, 2)

# Envoyer la réponse au serveur
s.sendall(f"{final_result}\n".encode())

# Recevoir la réponse du serveur (si nécessaire)
response = s.recv(1024).decode()
print(f"Réponse du serveur : {response}")

# Fermer la connexion
s.close()