#/******************************************************************************
# 
#  Copyright (c) 2018 Antillia.com TOSHIYUKI ARAI. ALL RIGHTS RESERVED.
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
 
# 2019/04/30
# 2019/09/13 Updated to use ZImageClassifierView

# On CIFAR-10 dataset, see the following page:

# http://www.cs.toronto.edu/~kriz/cifar.html

# See also:
# https://github.com/ageron/tensorflow-models/blob/master/slim/datasets/download_and_convert_cifar.py

#  ImageClassifier.py

# encodig: utf-8

import sys
import os
import time
import traceback

sys.path.append('../../')

from SOL4Py.ZImageClassifierView import *

from ImageModel import *


############################################################
# Classifier View

class MainView(ZImageClassifierView):  
  # Class variables

  # ClassifierView Constructor
  def __init__(self, title, x, y, width, height):
    super(MainView, self).__init__(title, x, y, width, height,
             datasets={"ImageModel": ImageModel.IMAGE_MODEL})
    
    self.model_loaded = False
    # keras.preprocessing.image
    self.image       = None
 
    self.image_size  = (ImageModel.IMAGE_WIDTH, ImageModel.IMAGE_HEIGHT)


    # Load trained model
    
    self.model = ImageModel(self.dataset_id, mainv=self)
    if self.model.is_trained():
      self.model.create()
      self.model.load()
      self.model.compile()
      #self.model.evaluate()
      self.model_loaded = True
    else:
      print("You have to create a model file and weight file")
      print("Please run: python ImageModel.py " + str(self.dataset_id))
      QMessageBox.warning(self, "ImageClassifier", 
           "Model/Weight File Missing.\nPlease run: python ImageModel.py " + str(self.dataset_id))

    self.show()



############################################################
#    
if main(__name__):

  try:
    app_name  = os.path.basename(sys.argv[0])
    applet    = QApplication(sys.argv)
  
    main_view = MainView(app_name, 40, 40, 900, 500)
    main_view.show ()

    applet.exec_()

  except:
    traceback.print_exc()
    
