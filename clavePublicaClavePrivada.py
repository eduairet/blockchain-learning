'''Ejercicio práctico para comprender las llaves pública y privada con python'''

# Modulos necesarios para el script
from random import choice
from hashlib import sha256
from collections import namedtuple
from ecdsa import SigningKey

# Ejercicio de clave pública y privada
def generadorDeWallet():
    '''Esta función genera una wallet'''
    # Clave privada creada aleatoriamente que no debe ser compartida con nadie
    caracteresDeMensaje = 'ANCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz0123456789'
    mensajeRandom = ''.join([choice(caracteresDeMensaje) for i in range (64)])
    clavePrivada = sha256(bytes(mensajeRandom, encoding='utf-8')).hexdigest()
    # Clave pública generada de la clave privada
    clavePublica = sha256(bytes(clavePrivada, encoding='utf-8')).hexdigest()
    # Dirección de la wallet producto de un segundo digest
    direccion = sha256(bytes(clavePublica, encoding='utf-8')).hexdigest()
    return clavePrivada, clavePublica, direccion

# Namedtuple con estructura sencilla de wallet
Wallet = namedtuple('Wallet', ['clavePrivada', 'clavePublica', 'direccion'])
# Wallet del emisor
emisorWallet = Wallet(*generadorDeWallet())
print(emisorWallet)
# Wallet del receptor
receptorWallet = Wallet(*generadorDeWallet())
print(receptorWallet)

# Verificación utilizando ecdsa
# Tomado de https://www.educative.io/edpresso/how-to-verify-digital-signature-in-python-using-ecdsa-signingkey
clavePrivada = SigningKey.generate()
mensaje = "Hola amigo"
firma = clavePrivada.sign(bytes(mensaje, encoding='utf-8'))
print(firma)
clavePublica = clavePrivada.verifying_key
print("Verificado:", clavePublica.verify(firma, bytes(mensaje, encoding='utf-8')))
