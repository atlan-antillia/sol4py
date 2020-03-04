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
# AESFileCipher.py

# encoding: utf-8

import os
import sys
import base64
import traceback
import filecmp

sys.path.append('../')

from SOL4Py.crypto.ZAESFileCipher import *


if __name__ == '__main__':
    try:
        filecipher = ZAESFileCipher()
        in_filename  = "test.txt"
        enc_filename = "enc_test.txt"
        dec_filename = "dec_test.txt"

        key = '1998key!C#$X%asZpo()/?'
        iv = Random.get_random_bytes(AES.block_size)
        
        filecipher.encrypt(in_filename, enc_filename, key, iv)

        filecipher.decrypt(enc_filename, dec_filename, key, iv)
        
        is_same = filecmp.cmp(in_filename, dec_filename)
        print('Input file:    {} {}(bytes) \nDecrypted file:{} {}(bytes)  \nare same? {}'.format(
                         in_filename,  os.path.getsize(in_filename),
                         dec_filename, os.path.getsize(dec_filename),
                         is_same))
        print("")

        key = 'key!C#$X%asZpo()tokyo2020/?'
        iv = Random.get_random_bytes(AES.block_size)
        in_filename  = "TOKYO2020.JPG"
        enc_filename = "XENC_TOKYO2020.enc"
        dec_filename = "XDEC_TOKYO2020.JPG"

        filecipher = ZAESFileCipher()

        filecipher.encrypt(in_filename, enc_filename, key, iv)
        
        filecipher.decrypt(enc_filename, dec_filename, key, iv)
        
        is_same = filecmp.cmp(in_filename, dec_filename)
        print('Input file:    {} {}(bytes) \nDecrypted file:{} {}(bytes)  \nare same? {}'.format(
                         in_filename,  os.path.getsize(in_filename),
                         dec_filename, os.path.getsize(dec_filename),
                         is_same))
        
    except:
        traceback.print_exc()
    


