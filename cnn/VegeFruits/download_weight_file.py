#/******************************************************************************
# 
#  Copyright (c) 2019 Antillia.com TOSHIYUKI ARAI. ALL RIGHTS RESERVED.
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
 
# 2019/05/19

#  download_weight_file.py

# If you would like to download the weight file "VegeFruitsModel_0.h5"
# from antillia.com
# Please run this script file.


# encodig: utf-8

import sys
import os
import time
import traceback
import numpy as np
import zipfile

sys.path.append('../../')

from SOL4Py.ZMain import *


if main(__name__):
  try:
    weight_file = "VegeFruitsModel_0.h5"

    if os.path.exists(weight_file) != True:
      from keras.utils.data_utils import get_file
      zip_file = "VegeFruitsModel_0.zip"
    
      url      = "http://www.antillia.com/sol4py/store/" + zip_file
      zip_file = get_file(zip_file, url)
      print("You have downloaded {}".format(zip_file))

      with zipfile.ZipFile(zip_file) as zf:
        zf.extractall()
    else:
      print("OK, you have the weight file {}!".format(weight_file))
       
  except:
    traceback.print_exc()



