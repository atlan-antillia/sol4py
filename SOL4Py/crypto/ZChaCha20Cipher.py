#/******************************************************************************
# 
#  Copyright (c) 2020 Antillia.com TOSHIYUKI ARAI. ALL RIGHTS RESERVED.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#******************************************************************************/

# 2020/01/30
# ZChaCha20Cipher.py

# encoding: utf-8

# pip install pycryptodome

# See also https://pycryptodome.readthedocs.io/en/latest/src/cipher/chacha20.html

import base64
import traceback
import sys
import binascii

from Crypto import Random
from Crypto.Cipher import ChaCha20

import traceback

from SOL4Py.crypto.ZCipher import *

class ZChaCha20Cipher(object):
    
    KEY_SIZE    = 32
    NONCE_SIZE  = 12
    
    # The constructor
    def __init__(self):
        pass

        
    # This method will encrypt raw data(str or bytes)  by key and iv.
    # key may be created by Random.get_random_bytes(self.KEY_SIZE)  #32
    # nonce may be create by Random.get_random_bytes(self.NONCE_SIZE)    #12
    #   See https://tools.ietf.org/html/rfc7539
    # and pass it to this method.
    def encrypt(self, data, key, nonce):
        if type(data) is str:
           data = data.encode('utf-8')
        cipher = ChaCha20.new(key = key, nonce=nonce)
        encrypted  = cipher.encrypt(data)
        return encrypted
            
            
    # This method will decrypt encrypted data  by key.
    # key should be a key when used to encrypt data.
    # nonce should be a nonce when used to encrypt data
    def decrypt(self, encrypted, key, nonce):
        cipher = ChaCha20.new(key = key, nonce = nonce)
        decrypted = cipher.decrypt(encrypted)
        return decrypted

    def generate_nonce(self):
        return Random.get_random_bytes(self.NONCE_SIZE)
        
    def hex(self, data):
        return binascii.hexlify(data)

    def unhex(self, data):
        return binascii.unhexlify(data)

    def b64encode(self, data):
      return base64.b64encode(data)
      
    def b64decode(self, data):
      return base64.b64decode(data)

