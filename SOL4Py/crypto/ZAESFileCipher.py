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
# ZAESFileCipher.py

import traceback

from SOL4Py.crypto.ZAESCipher import *

class ZAESFileCipher(ZAESCipher):
    
    # The constructor
    def __init__(self):
        super().__init__()

    # This method will read a file, and decrypt the read data by key and iv, and save it to another file.
    # key may be any text string.
    # iv should be a binary byte array, for example Random.get_random_bytes(AES.block_size)
    def encrypt(self, in_filename, out_filename, key, iv):
        #This is a very simple method, but not suitable for a large file
        with open(in_filename, "rb" ) as infile:
            data = infile.read()
        encrypted = super().encrypt(data, key, iv)

        with open(out_filename, "wb" ) as outfile:
            outfile.write(encrypted)


    # This method will read a file, and decrypt the read data by key and iv, and save it to another file.
    #
    # key may be any text string.
    # iv should be a binary byte array, for example Random.get_random_bytes(AES.block_size)
    def decrypt(self, in_filename, out_filename, key, iv):
        #This is a very simple method, but not suitable for a large file
        with open(in_filename, "rb") as infile:
            data = infile.read()

        decrypted = super().decrypt(data, key, iv)

        with open(out_filename, "wb") as outfile:
            outfile.write(decrypted)


