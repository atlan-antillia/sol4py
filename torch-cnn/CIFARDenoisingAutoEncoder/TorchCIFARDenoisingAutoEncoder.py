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
 
# 2019/07/23

#  TorchCIFARDenosingAutoEncoderModel.py

# encodig: utf-8

import sys
import os
import time
import traceback
import random
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageOps, ImageFilter

import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

import torchvision.transforms as transforms
from torch.utils.data import DataLoader

sys.path.append('../../')


from SOL4Py.ZMLModel import *
from SOL4Py.ZMain    import *
from SOL4Py.ZGaussianNoiseInjector import ZGaussianNoiseInjector
from SOL4Py.ZPILGaussianNoise import ZPILGaussianNoise


from SOL4Py.torch.ZTorchSimpleAutoEncoderModel import ZTorchSimpleAutoEncoderModel
from SOL4Py.torch.ZTorchEpochChangeNotifier import ZTorchEpochChangeNotifier
from SOL4Py.torch.ZTorchModelCheckPoint import ZTorchModelCheckPoint

sys.path.append('../')

from CIFARAutoEncoder.TorchCIFARAutoEncoder import TorchCIFARAutoEncoder

# Define TorchCIFARDenosingAutoEncoder derived from TorchCIFARAutoEncoder,
# because there are quite similar interfaces between them.


CIFAR10  = 0
CIFAR100 = 1


class TorchCIFARDenoisingAutoEncoder(TorchCIFARAutoEncoder):

  ##
  # Constructor
  def __init__(self, dataset_id = CIFAR10, 
                     epochs=20, mainv=None, ipaddress="127.0.0.1", port=8888):

    super(TorchCIFARDenoisingAutoEncoder, self).__init__(dataset_id, epochs, mainv, ipaddress, port)

    self.model_filename  = self.__class__.__name__ + "_" + str(self.dataset_id) + ".pt"

    
  # Create training and validation transformers with ZPILGaussianNoise.
  def create_image_transformer(self):
    self.train_transformer = transforms.Compose([
                        ZPILGaussianNoise(40),
                        transforms.ToTensor(),])
     
    self.valid_transformer = transforms.Compose([
                        ZPILGaussianNoise(40),
                        transforms.ToTensor(),])


#################################################
#
if main(__name__):

  try:
    app_name  = os.path.basename(sys.argv[0])
   
    dataset_id = 0
    epochs     = 20

    if len(sys.argv) >=2:
      dataset_id = int(sys.argv[1])
    
    if len(sys.argv) ==3:
      epochs = int(sys.argv[2])

    model = TorchCIFARDenoisingAutoEncoder(dataset_id = dataset_id, epochs = epochs)
    model.build()

    sampling = 10
    decoded_images = model.predict(model.valid_loader,    n_sampling=sampling)
    model.show_images(model.valid_loader, decoded_images, n_sampling=sampling)

  except:
    traceback.print_exc()

