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
 
#  CustomImageDataGenerator.py

# 2019/07/16 

# encodig: utf-8
import os
import sys
import glob


from PIL import Image, ImageOps

sys.path.append('../../')

from SOL4Py.ZMain  import *
from SOL4Py.ZCustomImageDataGenerator  import *

"""
class ZCustomImageDataGenerator:

  def __init__(self,  rotation_angle=10, left_top_position=(10, 10), shrink_size=(95, 95), 
       affine_shift_position=(0.25, 0.1), contrast=0.3, saultpepper_noise = 0.02, crop_size=300,
       sharpening=True, smoothing=True, edge_enhancing=True, horizontal_flip=True, vertical_flip=False):

"""


##############################################################
#
#          
if main(__name__):

  try:
    image_folder  = "./base_images/*/*.jpg"
    save_folder   = "./augmented/"

    #image_folder = "./mini_dataset/*/*.png
    #image_folder = "./mini_dataset/train/*/*.jpg"
    #save_folder  = "./dataset/train/"

    generator = ZCustomImageDataGenerator(rotation_angle=10, left_top_shift=(8, 8), shrink_ratio=(0.95, 0.90), crop_size=128)

    # To save augmented images to output_folder, specify output_folder parameter
    flow = generator.flow_from_directory(image_folder=image_folder, save_folder=save_folder, n_augmentation=25)

    # No generated images are saved as files, for save_folder parameter is not given.
    #flow = generator.flow_from_directory(image_folder=image_folder, n_augmentation=25)

    for i in flow:
      image = next(flow)
      print("generated {} image size: {}".format(i, image.size))
      
  except:
    traceback.print_exc()
  else:
    pass
    
  finally:
   pass
      


