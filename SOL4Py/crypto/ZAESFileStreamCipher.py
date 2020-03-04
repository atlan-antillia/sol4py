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
# ZAESFileStreamCipher.py

# See also: https://eli.thegreenplace.net/2010/06/25/aes-encryption-of-files-in-python-with-pycrypto
import os
import traceback

from SOL4Py.crypto.ZAESCipher import *

class ZAESFileStreamCipher(ZAESCipher):
    # Ecrypted file format: filesize_bytes(6) +  iv(AES.block_size) + encrypted_data
    
    FILE_SIZE  = 6                #Byte size to store a size of file to be encrypted
    BYTE_ORDER = 'little'         #Byte-order specifiter 
                                  # to convert integer to bytes, and bytes to integer.
    IV_SIZE    = AES.block_size   #Byte size of AES iv(initial vector)

    FILE_BLOCK_SIZE = AES.block_size * 1024 #Byte size to be read from a file, which must be multiple of AES.block_size
    
    # The constructor
    def __init__(self):
        super().__init__()


    def encrypt(self, in_filename, out_filename, key):

        with open(in_filename, "rb" ) as infile:
            in_filesize = os.path.getsize(in_filename)

            with open(out_filename, "wb" ) as outfile:
                enc_key = SHA256.new(key.encode()).digest()
                iv = Random.get_random_bytes(AES.block_size)
                # Create AES cipher object from the enc_key and iv
                cipher = AES.new(enc_key, self.mode, iv)

                filesize = in_filesize.to_bytes(self.FILE_SIZE, self.BYTE_ORDER)

                outfile.write(filesize)
                outfile.write(iv)

                while True:
                   
                    data = infile.read(self.FILE_BLOCK_SIZE)
                    data_len = len(data)
                    if data_len == 0:
                        break
                    elif data_len % AES.block_size != 0:
                        #print("padding")
                        data = Padding.pad(data, AES.block_size, self.padding_alg)
                    #Encrypt data by cipher and write the encrypted to the outfile
                    encrypted = cipher.encrypt(data)
                    outfile.write(encrypted)


    def decrypt(self, in_filename, out_filename, key):

        with open(in_filename, "rb") as infile:
            filesize_bytes = infile.read(self.FILE_SIZE)
            filesize = int.from_bytes(filesize_bytes, self.BYTE_ORDER)
            iv = infile.read(self.IV_SIZE)
            
            with open(out_filename, "wb") as outfile:
                enc_key = SHA256.new(key.encode()).digest()
                # Create AES cipher object from the enc_key and iv
                cipher = AES.new(enc_key, self.mode, iv)

                while True:
                    data = infile.read(self.FILE_BLOCK_SIZE)
                    data_len = len(data)
                    if data_len == 0:
                        break

                    # Decrypte data, and write it to the outfile.
                    decrypted = cipher.decrypt(data)

                    outfile.write(decrypted)
                    # Truncate the outfile to be the original filesize
                    outfile.truncate(filesize)

