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
# AESIVEmbeddedCipher.py

# encoding: utf-8

import os
import base64
import traceback
import sys

sys.path.append('../')

from  SOL4Py.crypto.ZAESIVEmbeddedCipher import *


if __name__ == '__main__':
    try:
        cipher = ZAESIVEmbeddedCipher(ZCipher.AS_HEX)
        key = '!C#$X%asZpo()/?sun'        
        text = 'Antarctica will contribute about a foot of sea-level rise by 2100.'
        
        encrypted = cipher.encrypt(text, key)
            
        decrypted = cipher.decrypt(encrypted, key)
        decrypted = decrypted.decode('utf-8')
        print("AS_HEX format...")
        print("Text:     '{}'".format(text))
        print("Decrypted:'{}'".format(decrypted))
        print("")

        btext = b'The global warming is real. Welcome to TOKYO2020 in the hottest summer of Japan.'
        key = '&=~|%asZpo()/?moon'
        cipher = ZAESIVEmbeddedCipher(ZCipher.AS_BASE64)
        
        encrypted = cipher.encrypt(btext, key)
        decrypted = cipher.decrypt(encrypted, key)
        
        print("AS_BASE64 format...")
        print("Text:     '{}'".format(btext))
        print("Decrypted:'{}'".format(decrypted))
        print("")

        key = '=~#$X%asZpo()/?mars'
        cipher = ZAESIVEmbeddedCipher(ZCipher.AS_JSON)
        
        encrypted = cipher.encrypt(btext, key)
        decrypted = cipher.decrypt(encrypted, key)
        
        print("AS_JSON format...")
        print("Text:     '{}'".format(btext))
        print("Decrypted:'{}'".format(decrypted))
        print("")

        key = '%$#<>`{]po()/?pluto'
        cipher = ZAESIVEmbeddedCipher(ZCipher.AS_BINARY)
        
        encrypted = cipher.encrypt(btext, key)
        decrypted = cipher.decrypt(encrypted, key)
        
        print("AS_BINARY format...")
        print("Text:     '{}'".format(btext))
        print("Decrypted:'{}'".format(decrypted))
        print("")

    except:
        traceback.print_exc()
    


