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
# ZAESFileBatchCipher.py

import traceback

from SOL4Py.crypto.ZAESFileCipher import *

class ZAESFileBatchCipher(ZAESCipher):

    # encrpted file format: iv + real_encrypted_data

    # The constructor
    def __init__(self):
        super().__init__()

    # This method will read a file into a memory in a lump, and decrypt the read data by key and iv, 
    # and save it to another file.
    # key may be any text string.
    # iv is generated automaticall in this method, and embedded to the ecnrypted file as something like this:
    # iv + real_encrypted__data
    def encrypt(self, in_filename, out_filename, key):
        #This is a very simple method, but not suitable for a large file
        with open(in_filename, "rb" ) as infile:
            data = infile.read()
        # Generate iv 
        iv = Random.get_random_bytes(AES.block_size)
        encrypted = super().encrypt(data, key, iv)
        iv_encrypted = iv + encrypted
        with open(out_filename, "wb" ) as outfile:
            outfile.write(iv_encrypted)
      
 
    # This method will read a file into a memory in a lump, and decrypt the read data by key and iv, 
    # and save it to another file.
    #
    # key may be any text string.
    # iv is read from the input file.
    def decrypt(self, in_filename, out_filename, key):
        #This is a very simple method, but not suitable for a large file
        with open(in_filename, "rb") as infile:
            encrypted = infile.read()

        # Extract iv from the encrpted bytes.
        iv = encrypted[:AES.block_size]
        # Extrat the real encrypted data from the encrypted
        encrypted = encrypted[AES.block_size:]

        decrypted = super().decrypt(encrypted, key, iv)

        with open(out_filename, "wb") as outfile:
            outfile.write(decrypted)

