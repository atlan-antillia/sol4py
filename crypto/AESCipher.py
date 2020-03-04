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
# AESCipher.py

# encoding: utf-8

import base64
import traceback
import sys

sys.path.append('../')

from  SOL4Py.crypto.ZAESCipher import *


if __name__ == '__main__':
    try:
        cipher = ZAESCipher()
        key = 'TOKYO!C#$X%asZpo()/?'
        iv = Random.get_random_bytes(AES.block_size)
        
        text = 'Antarctica will contribute about a foot of sea-level rise by 2100.'
        
        encrypted = cipher.encrypt(text, key, iv)
        #print("Encrypted:'{}'".format(encrypted))
            
        decrypted = cipher.decrypt(encrypted, key, iv)
        
        utf8_decrypted = decrypted.decode('utf-8')
        
        print("UTF8Text:     '{}'".format(text))
        print("UTF8Decrypted:'{}'".format(utf8_decrypted))
        print("")

        btext = b'The global warming is real. Welcome to TOKYO2020 in the hottest summer of Japan.'
        key = 'Warming!C#$X%asZpo()/?'
        iv = Random.get_random_bytes(AES.block_size)
        
        encrypted = cipher.encrypt(btext, key, iv)
        #print("Encrypted:'{}'".format(encrypted))
            
        decrypted = cipher.decrypt(encrypted, key, iv)
        
        
        print("OriginalBytes: '{}'".format(btext))
        print("DecryptedBytes:'{}'".format(decrypted))
        print("")

    except:
        traceback.print_exc()
    


