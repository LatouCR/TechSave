#LIBRERIAS NECESARIAS
import numpy as np #numpy es una de las librerias más famosas de Python. Tiene muchas funcionalidad numericas.

import crypt
from random import random
from random import randint
from random import seed
from random import sample

def key(mensaje):
    """Esta funcion genera una llave pseudo-aleatoria de la misma longitud del mensaje."""
    key = []
    # ----------------Declaracion de variables libreta--------------------#
    abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                  'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r',
                  's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    numeros_primos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # suma importancia para la generacion de la llave

     #simbolos = ['@', '$', '^', '&', '*', '(', ')', '_', '+', ':', '£', '?', '~']

    # combined = np.vstack((abecedario, numeros_primos)).T  #--> esto lo combierten matriz 2D
    combined = np.append(abecedario, numeros_primos)  # unimos los dos arreglos en uno solo 1D.
   #  combined=np.append(combined,simbolos) #Podriamos agregarle simbolos
    np.random.shuffle(combined)  # Esto hace un shuffle.
   
    # ----------------creación de semilla pseuda-aleatoria---------#
    seed = []
    for i in range(500):
        seed.append(randint(0, 36))

    subset = sample(seed, len(mensaje))
    # ----------------Creación de key-------------------------------#

    for i in range(len(subset)):
        key.append(combined[subset[i]])

    return listToString(key) # retorno de la llave

def listToString(s):
    """Funcion que permite pasar de una variable tipo lista a string"""
    # initialize an empty string
    str1 = ""
    # traverse in the string
    for ele in s:
        str1 += ele
    # return string
    return str1


def encrypt(key,mensaje):
  """Funcion que cifra el mensaje mediante una funcion XOR con la llave. Retorna un ciphertext"""
  cipher=""
  for i in range(len(mensaje)):
    t = mensaje[i]
    k = key[i%len(key)]
    x = ord(k) ^ ord(t)
    cipher += chr(x) #Vamos añadiendo los valores producto del XOR al cipher.
  return cipher.encode("utf-8").hex() #Retorna el ciphertex en HEXADECIMAL

def decrypt(key, ciphertext):
  """Funcion de descripcion, realiza una funcion XOR entre el ciphertext y la llave y retorna el mensaje original"""
  a_string = bytes.fromhex(ciphertext)
  a_string = a_string.decode("utf-8")
  mensaje = ""
  for i in range(len(a_string)):
    t = a_string[i]
    k = key[i%len(key)]
    x = ord(k) ^ ord(t)
    mensaje += chr(x)
  return mensaje

"All logic methods above"

def menu ():


      validador = False #valore necesario para validacion menu
      #valores necesarios        
      registro_keys = []
      registro_cipher = []
#Inicio del loop para el menu principal
      while True:
        

        print ("Laboratorio Ethical Hacking #1")
        print ("1. Cifrar un mensaje")
        print ("2. Descifrar un mensaje")
        print ("3. Salir")

        option = input("Ingresa la opción: ")

        if option == "1":
            mensaje = input("Digite el mensaje que quiere encriptar: \n")
            key_program = key(mensaje) #mando la informacion para hacer la llave
            registro_keys.append(key_program) #se registra la llave.
            cipher_text = encrypt(key_program,mensaje) #con la llave encripto el mensaje
            registro_cipher.append(cipher_text) #Guardo el mensaje encriptado
            print("El mensaje encriptado es el siguiente: \n", cipher_text)
            validador = True

        elif option == "2":

            if (validador == True ):
                print("El mensaje Decifrado es el Siguiente: \n")
                mensaje_decrypt = decrypt(key_program, cipher_text) #mensaje con la llave es decifrado
                print (mensaje_decrypt)
            else:
                 print ("Debe Cifrar un mensaje primero \n")

        elif option == "3":
                print("Muchas gracias\n")
                break
        else:
                print("Ninguna opción es valida\n")

#Menu running
menu()
