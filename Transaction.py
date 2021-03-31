from __future__ import unicode_literals
import base64
import os
import Crypto.Random.OSRNG.posix as RNG
import hashlib

import six
from Crypto import Random
from Crypto.PublicKey import RSA

class Transaction:
  def__init__(self):
    self.input_transaction = []
    self.output_transaction1 = []
    self.output_transaction2 = []
 
def randomCryptoNumber():
    return RNG.new().read(AES.block_size) #Retourne un nombre aléatoire

  
  def append_data(data):
    # si la taille de donnée fait 16 byte, aucun ajout
    if len(data) % 16 == 0:
        return data

    # On enlève un byte pour ajouter le 0x80

    dataAppend = 15 - (len(data) % 16)

    data = '%s\x80' % data
    data = '%s%s' % (data, '\x00' * dataAjouter)

    return data  
  
  def remove_data(data):
  if not data:
      return data

  data = data.rstrip('\x00')
  if data[-1] == '\x80':
      return data[:-1]
  else:
      return data
  
 

def generateCryptoKey():
    key_size = 32
    key = str(RNG.new().read(key_size))
    return key  
  
 import Crypto.Cipher.AES as AES

def encrypt(data, key):

  #Encrypte les donnée utilisant AES en mode CBC

  data = ajout_data(data)
  number = randomCryptoNumber()
  aes = AES.new(key, AES.MODE_CBC, number)
  msg_crypt = aes.encrypt(data)

  return number + msg_crypt

def decrypt(ciphertext, key):

  #Decrypt un ciphertext encrypté avec l'AES en mode CBC

  if len(ciphertext) <= AES.block_size:
      raise Exception("Invalid ciphertext.")
  number = ciphertext[:AES.block_size]
  ciphertext = ciphertext[AES.block_size:]
  aes = AES.new(key, AES.MODE_CBC, number)
  data = aes.decrypt(ciphertext)

  return desajout_data(data) #Enleve le padding ajouter 
  
def hash384(transaction)
  hash384 = hashlib.sha1(transaction).hexdigest() 


  
  
  def new_transaction(self,sender_public,sender_private,recipient,amount)
