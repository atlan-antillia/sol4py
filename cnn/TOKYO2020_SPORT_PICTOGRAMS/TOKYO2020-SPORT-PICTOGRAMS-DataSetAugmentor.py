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

# TOKYO2020-SPORT-PICTGRAMS-DataSetAugmentor.py

# 2019/05/13

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
       
    augmentation = 10
    
    # To create images for training or validation, please specify 
    # target as "./dataset/train" or "./dataset/valid".
    target       = "./dataset/train"
    
    # To generate images for testing from ./mini_dataset".
    target       = "./test"

    if len(sys.argv) ==2:
      augmentation = int(sys.argv[1])
 
    if len(sys.argv) ==3:
      augmentation = int(sys.argv[1])
      target       = str(sys.argv[2])

    mini_dataset       = ("./mini_dataset",  "png")
    augmented_dataset  = (target,            "png")

    print("augmentation:      " + str(augmentation))
    print("mini_dataset:      " + str(mini_dataset))
    print("augmented_dataset: " + str(augmented_dataset))
       
    # 1 Generate augmented images from mini_dataset folder,  and save them to augmented_dataset folder.
    generator = ImageDataGenerator( 
                                        #rescale           = 1.0 /255, 
                                        rotation_range     = 20,
                                        width_shift_range  = 1.0,
                                        height_shift_range = 0.3,
                                        shear_range        = 0.4,
                                        zoom_range         = 0.3,
                                        brightness_range   = [0.7,1.2],
                                        channel_shift_range= 2.0,
                                        horizontal_flip    = False,  # We dont' flip pictograms images horizontally or vertically. 
                                        vertical_flip      = False)

    augmentor = ZDataSetAugmentor(generator)
    augmentor.generate(mini_dataset, augmented_dataset, n_augmentation=augmentation)
    
 
    # 2 Load the augmented_dataset
    loader    = ZDataSetLoader()
    loader.load_dataset(augmented_dataset)
    
    loader.show_summary()
    
  except:
    traceback.print_exc()


