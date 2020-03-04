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

# Torch_TOKYO2020_SPORT_PICTOGRAMS_DataSetAugmentor.py

# 2019/07/13

# encodig: utf-8

import sys
import os
import time
import traceback
 
sys.path.append('../../')

from SOL4Py.ZMain import *
from SOL4Py.ZCustomImageDataGenerator import *


############################################################
#  

if main(__name__):

  try:
    app_name  = os.path.basename(sys.argv[0])
       
    #augmentation = 10  # for validation dataset  
    augmentation = 100   # for train dataset
    
    # To create images for training or validation, please specify 
    # target as "./dataset/train" or "./dataset/valid".
    target       = "./dataset/train"
    
    if len(sys.argv) ==2:
      augmentation = int(sys.argv[1])
 
    if len(sys.argv) ==3:
      augmentation = int(sys.argv[1])
      target       = str(sys.argv[2])  #"./dataset/train" or "./dataset/valid"

    base_dataset       = "./base_dataset/*/*.png"  # Each category folder contains only one roadsign png file. 
    augmented_dataset  = target                               # "./dataset/train" or "./dataset/valid"

    print("augmentation:      " + str(augmentation))
    print("base_dataset:      " + str(base_dataset))
    print("augmented_dataset: " + str(augmented_dataset))
       
    # 1 Generate augmented images from mini_dataset folder,  and save them to augmented_dataset folder.
    generator = ZCustomImageDataGenerator(rotation_angle=6, 
                                        crop_size = 128, 
                                        background=(255,255,255),
                                        horizontal_flip    = False,  # We dont' flip pictograms images horizontally or vertically. 
                                        vertical_flip      = False)
                                        
    # To save augmented images to output_folder, specify output_folder parameter
    flow = generator.flow_from_directory(image_folder=base_dataset, save_folder=target, save_format="jpg", n_augmentation=augmentation)
    
    for i in flow:
      image = next(flow)
      print("generated {} image size: {}".format(i, image.size))
    
  except:
    traceback.print_exc()


