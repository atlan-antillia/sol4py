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

# 2019/07/13 

#  Torch_TOKYO2020_SPORT_PICTOGRAMS_Dataset.py

# See: https://github.com/pytorch/tutorials/issues/78

import os
import glob
import traceback

from random import *
import numpy as np

from torch.utils.data.dataset import Dataset
from torch.utils.data import DataLoader
import torchvision.transforms

from scipy.io import loadmat
from PIL import Image

class Torch_TOKYO2020_SPORT_PICTOGRAMS_Dataset(Dataset):

  #TRAIN_DATA_DIR = "./dataset/train/"
  #VALID_DATA_DIR = "./dataset/valid/"


  ##
  # Constructor
  # 
  def __init__(self,  transform =None, root="./dataset/train/", image_file_extension = "jpg",):
      self.transform = transform
      self.images  = None
      self.root        = root
      self.image_folder = self.root + "/*/*." + image_file_extension
      
      files = glob.glob(self.image_folder)   # image_folder  = "./dataset/*/*.jpg"
      self.filenames_list = sorted(files)
      
      self.classes   = sorted( os.listdir(self.root) )
      self.nclasses = len(self.classes)
      print("NCLASSES {}".format(self.nclasses))
      

  def __getitem__(self, index):
      filename = self.filenames_list[index]
      image = Image.open(filename).convert('RGB')
      classname  = os.path.basename(os.path.dirname(filename))
      #print("category {}".format(classname))
      class_index = self.get_class_index(classname)
     
      if self.transform is not None:
         image = self.transform(image)
      return image, class_index


  def __len__(self):
    l = len(self.filenames_list)
    return l
    

  def get_class_index(self, classname):
    index = 0
    for i in range(len(self.classes)):
      if self.classes[i] == classname:
        index = i
        break
    return index


############################################################
#    

if __name__ == "__main__":

  try:
    path = "./class_names.txt"
   
    dataset = Torch_TOKYO2020_SPORT_PICTOGRAMS_Dataset()
    classes = dataset.classes
    with open(path, "w") as file:
      for name in classes:
        print(name)
        file.write("{}\n".format(name))    

  except:
    traceback.print_exc()
  
  