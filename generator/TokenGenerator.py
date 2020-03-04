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

# encoding: utf-8
# 2020/01/30

# TokenGenerator.py

import sys
import numpy as np

sys.path.append('../')
from SOL4Py.generator.ZTokenGenerator import *

###
#---------------------------------------------------------  

if __name__ == "__main__":
  generator = ZTokenGenerator()
  
  for i in range(20):
    name = generator.generate(20)
    print("{} Token: {}".format(i, name))
    
    