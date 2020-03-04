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

# ZPasswordGenerator

# This is NOT using yield.
# encoding: utf-8

# See https://stackoverflow.com/questions/3854692/generate-password-in-python

import sys
import secrets
import numpy as np
import string
import random

sys.path.append('../')

from SOL4Py.generator.ZGenerator import ZGenerator


###
#---------------------------------------------------------  
class ZPasswordGenerator(ZGenerator):
  ##
  # Constructor
  def __init__(self):
    pass


  def generate(self, size=10):
    letters = string.printable.strip()
    password = ''
    
    for i in range(size):
      #It's much better to use secrets than random
      password += secrets.choice(letters)
      #password += random.choice(letters)
    return password 


if __name__ == "__main__":
  generator = ZPasswordGenerator()
  
  for i in range(20):
    name = generator.generate(12)
    print(name)

 
    