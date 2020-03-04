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
# ZTokenGenerator.py

# encoding: utf-8

import os

class ZTokenGenerator:
   DEFAULT_LENGTH = 16
   
   def __init__(self):
     pass
  
   #Generate a random bytes array of hex format with specified byte size.
   def generate(self, size):
       if size <self.DEFAULT_LENGTH:
           size = self.DEFAULT_LENGTH
           
       return os.urandom(size).hex()
           
   # Usage
   # generator = ZTokenGenerator()
   # twentybytes_random_token = generator(20)
   # which may not be a real unique token, but it may be much better than ordinary uuid4 of 16bytes.   
