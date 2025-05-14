from Crypto.Util.number import *
import gmpy2
import base64

p = getPrime(50)
print('1', p)
q = getPrime(50)
print('2', q)
N = p * q
print('3', N)
e = 65537
#print('4', e)
m = bytes_to_long(b"salut")
#print('5', m)
c = (m**e) % N
print('6', c)

phi = (p-1)*(q-1)
#print('7', phi)
d = inverse(e,phi)
#print('7', d)
m = pow(c,d,N)
#print('8', m)

cipher_base64 = base64.b64encode(long_to_bytes(c)).decode('utf-8')
print("Texte chiffré (base64) :", cipher_base64)
print('decrypt > ', long_to_bytes(m))