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

from  SOL4Py.crypto.ZChaCha20Cipher import *


if __name__ == '__main__':
    try:
        cipher = ZChaCha20Cipher()
        key   = Random.get_random_bytes(ZChaCha20Cipher.KEY_SIZE)
        nonce = Random.get_random_bytes(ZChaCha20Cipher.NONCE_SIZE)
                
        text = 'Antarctica will contribute about a foot of sea-level rise by 2100.'
        
        encrypted = cipher.encrypt(text, key, nonce)
            
        decrypted = cipher.decrypt(encrypted, key, nonce)
        
        utf8_decrypted = decrypted.decode('utf-8')
        
        print("UTF8Text:     '{}'".format(text))
        print("UTF8Decrypted:'{}'".format(utf8_decrypted))
        print("")

        btext = b'The global warming is real. Welcome to TOKYO2020 in the hottest summer of Japan.'
        key   = Random.get_random_bytes(ZChaCha20Cipher.KEY_SIZE)
        nonce = Random.get_random_bytes(ZChaCha20Cipher.NONCE_SIZE)
        
        encrypted = cipher.encrypt(btext, key, nonce)
            
        decrypted = cipher.decrypt(encrypted, key, nonce)
        
        print("OriginalBytes: '{}'".format(btext))
        print("DecryptedBytes:'{}'".format(decrypted))
        print("")

    except:
        traceback.print_exc()
    


