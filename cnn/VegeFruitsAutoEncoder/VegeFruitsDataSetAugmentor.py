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

# VegeFruitsDataSetAugmentor.py

# 2019/04/22

# encodig: utf-8

import sys
import os
import time
import traceback
import keras
 
sys.path.append('../../')

from SOL4Py.ZMain import *
from SOL4Py.keras.ZDataSetAugmentor import *
from SOL4Py.keras.ZDataSetLoader import *


############################################################
#  

if main(__name__):

  try:
    app_name  = os.path.basename(sys.argv[0])
       
    augmentation = 100
    
    if len(sys.argv) ==2:
      augmentation = int(sys.argv[1])
 
    
    mini_dataset       = ("./mini_dataset",      "jpg")
    augmented_dataset  = ("./augmented_dataset", "png")

    print("augmentation:      " + str(augmentation))
    print("mini_dataset:      " + str(mini_dataset))
    print("augmented_dataset: " + str(augmented_dataset))
       
    # 1 Generate augmented images from mini_dataset,  and save them to augmented_dataset.
    augmentor = ZDataSetAugmentor()
    augmentor.generate(mini_dataset, augmented_dataset, n_augmentation=augmentation)
    
 
    # 2 Load the augmented_dataset
    loader    = ZDataSetLoader()
    loader.load_dataset(augmented_dataset)
    
    loader.show_summary()
    
  except:
    traceback.print_exc()


