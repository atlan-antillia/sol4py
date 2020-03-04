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
# 2019/09/18

#  TorchVegeFruitsClassifier.py

# encodig: utf-8

import sys
import os
import time
import traceback
import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt
import numpy as np

sys.path.append('../../')

from SOL4Py.torch.ZTorchImagePreprocessor import ZTorchImagePreprocessor
from SOL4Py.ZTorchImageClassifierView import *

from TorchVegeFruitsModel import *

VEGEFRUITS = 0


############################################################
# Classifier View

class MainView(ZTorchImageClassifierView):  
  # Class variables

  # ClassifierView Constructor
  def __init__(self, title, x, y, width, height):
    super(MainView, self).__init__(title, x, y, width, height,
               datasets = {"VEGEFRUITS": VEGEFRUITS})
    
    self.model_loaded = False
    
    #self.class_names_set = [None, None]
    
    self.resize = 64 #128
    self.crop   = 64 #128

    self.image       = None
                           
    # Load trained model
    self.classes = self.get_class_names()
    
    self.model = TorchVegeFruitsModel(self.dataset_id, mainv=self)
    
    if self.model.is_trained():
      self.model.load_dataset()
      self.model.create()
      self.model.load()    # Load a trained weight
      #self.model.evaluate()
      self.model_loaded = True
    else:
      print("You have to create a model file")
      print("Please run: python TorchVegeFruitsModel.py " + str(self.dataset_id))
      QMessageBox.warning(self, "TorchVegeFruitsClassifier", 
           "Mode file is missing.\nPlease run: python TorchVegeFruitsModel.py " + str(self.dataset_id))

    self.show()


  def classify(self):
    self.write("--------------------------------------------")
    self.write("classify start.")
    self.write(self.filename)
    input = Variable(self.image_tensor)
    index = self.model.predict(input)

    label   = self.classes[index]
    self.write("Prediction: {}".format(label) )
    self.write("classify end.")


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
    
