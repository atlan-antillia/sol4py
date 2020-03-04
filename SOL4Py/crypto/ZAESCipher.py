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

# 2020/01/20
# ZAESCipher.py

# encoding: utf-8

# pip install pycryptodome

# https://gist.githubusercontent.com/5S/4b9179e6b71fb9a74b9c30fca266d7d2/raw/abb5a21d742ee8e315b490429cbb5bcc11272ae9/crypt.py
# See also https://pycryptodome.readthedocs.io/en/latest/src/util/util.html

import base64
import traceback
import sys
import binascii

from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util import Padding
from Crypto.Hash import SHA256
import traceback

from SOL4Py.crypto.ZCipher import *

class ZAESCipher(object):
    
    # The constructor
    def __init__(self):
        self.mode = AES.MODE_CBC
        self.padding_alg= 'pkcs7'  #– Padding algorithm. It can be ‘pkcs7’ (default)
        

    # This method will encrypt raw data(str or bytes)  by key and iv.
    # key may be any text string.
    # iv should be a binary byte array 
    #
    # In this implementation, you need to explicitly generate an initial vector(iv) 
    # by using Random module, something like this, Random.get_random_bytes(AES.block_size),
    # and pass it to this method.
    # The iv may be stored somewhere for example db, to decrypt the encryted data later.
    def encrypt(self, raw, key, iv):
        enc_key = SHA256.new(key.encode()).digest()

        cipher = AES.new(enc_key, self.mode, iv)
        if type(raw) == str:
            data = Padding.pad(raw.encode('utf-8'), AES.block_size, self.padding_alg)
        else:
            data = Padding.pad(raw, AES.block_size, self.padding_alg)
        bin_encrypted  = cipher.encrypt(data)
        return bin_encrypted

    # This method will decrypt encrypted binary data  by key and iv.
    # key may be any text string.
    # iv should be a binary byte array.
    def decrypt(self, bin_encrypted, key, iv):
        dec_key = SHA256.new(key.encode()).digest()
        cipher = AES.new(dec_key, self.mode, iv)
        decrypted = cipher.decrypt(bin_encrypted)
        bin_data = Padding.unpad(decrypted, AES.block_size, self.padding_alg)
        # return binary data
        return bin_data

    def hex(self, data):
        return binascii.hexlify(data)

    def unhex(self, data):
        return binascii.unhexlify(data)

    def b64encode(self, data):
      return base64.b64encode(data)
      
    def b64decode(self, data):
      return base64.b64decode(data)

