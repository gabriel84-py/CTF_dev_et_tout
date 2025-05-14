import re
import socket
import math
import base64
import time

# Connexion à la socket TCP
host = 'challenge01.root-me.org'
port = 51031

# Création de la socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

data = s.recv(1024).decode()

print(data)

time.sleep(2)

s.sendall(b"41662410494900335978865720133929900027297481493143223026704112339997247425350599249812554512606167456298217619549359408254657263874918458518753744624966096201608819511858664268685529336163181156329400702800322067190861310616")

print('ok')

data = s.recv(1024).decode()

print('ok')
print(data)