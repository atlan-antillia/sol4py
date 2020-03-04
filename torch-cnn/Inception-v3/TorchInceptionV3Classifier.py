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

# 2019/07/05

# Torch version

#  TorchInceptionV3Classifier.py

# See: https://pytorch.org/docs/master/torchvision/models.html#classification

# 
# encodig: utf-8

import sys
import os
import time
import traceback

sys.path.append('../../')

from SOL4Py.ZTorchImageClassifierView import *


DATASET_INCEPTIONV3 = 0

############################################################
# Classifier View

class MainView(ZTorchImageClassifierView):  
  # Class variables

  # ClassifierView Constructor
  def __init__(self, title, x, y, width, height):
    super(MainView, self).__init__(title, x, y, width, height,
            datasets = {"InceptionV3": DATASET_INCEPTIONV3})
    #  Load trained model
    self.write("Loading InceptionV3 model")
    
    self.model = models.inception_v3(pretrained=True)
    #  Change the self.model to aneval mode 
    self.model.eval()
    
    self.load_class_names()

    self.model_loaded = True
    
    self.write("Loaded InceptionV3 model")
    self.show()


  def load_class_names(self):
    class_index_file = './imagenet_class_index.json'
    self.write("load class index file {}".format(class_index_file))
    
    with open(class_index_file, 'r') as indexfile:
      class_index = json.load(indexfile)
      self.classes = {int(key):value[1] for (key, value) in class_index.items()}



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
    
