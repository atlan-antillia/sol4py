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
 
# 2019/05/13

#  MNISTDAE.py

# This is based on the following sample program.
# https://keras.io/examples/mnist_denoising_autoencoder/
# See also https://keras.io/datasets/

# encodig: utf-8

import sys
import os
import time
import traceback

import matplotlib.pyplot as plt
import numpy as np

import keras
import tensorflow as tf
from keras.utils import np_utils

sys.path.append('../')
from MNISTAutoEncoder.MNISTAutoEncoder import *


# Define MNISTDenosingAutoEncoder derived from MNISTAutoEncoder,
# because there are quite similar interfaces between them, 
# to load_data_set, to create  a model, to compile, to train and 
# to predict methods, apart from the input_data to be noise-injected or not.

class MNISTDenosingAutoEncoder(MNISTAutoEncoder):

  ##
  # Constructor

  def __init__(self, epochs, mainv=None, ipaddress="127.0.0.1", port=8888):
    super(MNISTDenosingAutoEncoder, self).__init__(epochs, mainv, ipaddress, port)


  # Weight file will be created in the current_dir, so you should define
  # set_weigth_filename method in each model class.
  # Build a full path name to a weight_file name from self.__class_.__name__ and currend_dir.
  def set_weight_filepath(self):
    weight_file = self.__class__.__name__ + "_"  + str(self.dataset_id) + ".h5" 
    current_dir = os.path.dirname(os.path.abspath(__file__))
    self.weight_filepath = os.path.join(current_dir, weight_file)
    print("weight_filepath:{}".format(self.weight_filepath))

  # Override supepr().load_dataset method to inject noise to the original x_train and x_test data. 
  def load_dataset(self):
    super().load_dataset()
   
    # Inject noise to the orginal dataset self.x_train and self.x_test.
    self.x_train = self.inject_noise_into(self.x_train)
    self.x_test  = self.inject_noise_into(self.x_test )


  # Redefine your own noise injection method if required.
  # See: https://keras.io/examples/mnist_denoising_autoencoder/
  def inject_noise_into(self, data):
    # Make Gaussian noise by using np.random.normal of size=data.shape
    noise = np.random.normal(loc=0.5, scale=0.5, size=data.shape)
    noised = data + noise
    return np.clip(noised, 0.0, 1.0)



#################################################
#
if main(__name__):

  try:
    app_name  = os.path.basename(sys.argv[0])

    epochs     = 10
    if len(sys.argv) == 2:
      epochs = int(sys.argv[1])

    model = MNISTDenosingAutoEncoder(epochs)
    model.build()
    
    model.predict()
    
    model.show_images()
    
  except:
    traceback.print_exc()

