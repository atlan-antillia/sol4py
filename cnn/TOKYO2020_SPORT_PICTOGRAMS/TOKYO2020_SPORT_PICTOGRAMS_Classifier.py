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
 
# 2019/05/13
# 2019/09/13 Updated load_file method not to use a temporary image file.


#  TOKYO2020_SPORT_PICTOGRAMS_Classifier.py

# encodig: utf-8

import sys
import os
import time
import traceback

from keras.preprocessing.image import load_img, img_to_array
from keras.utils.data_utils import get_file

sys.path.append('../../')

from SOL4Py.ZImageClassifierView import *

from TOKYO2020_SPORT_PICTOGRAMS_Model import *


############################################################
# Classifier View

class MainView(ZImageClassifierView):  
  # Class variables

  # ClassifierView Constructor
  def __init__(self, title, x, y, width, height):
    super(MainView, self).__init__(title, x, y, width, height,
                datasets={"PictogramModel": TOKYO2020_SPORT_PICTOGRAMS_Model.IMAGE_MODEL})
    
    self.model_loaded = False
    self.image_size = (TOKYO2020_SPORT_PICTOGRAMS_Model.IMAGE_WIDTH, 
                       TOKYO2020_SPORT_PICTOGRAMS_Model.IMAGE_HEIGHT)

    self.classes = self.get_class_names()
    
    self.model = TOKYO2020_SPORT_PICTOGRAMS_Model(self.dataset_id, mainv=self)
    if self.model.is_trained():
      self.model.create()
      self.model.load()
      self.model_loaded = True
    else:
      print("You have to create a weight file")
      print("Please run: python TOKYO2020_SPORT_PICTOGRAMS_Model.py " + str(self.dataset_id))
      QMessageBox.warning(self, "TOKYO2020_SPORT_PICTOGRAMS_Classifier", 
           "Weight File Missing.\nPlease run: python TOKYO2020_SPORT_PICTOGRAMS_Model.py " + str(self.dataset_id))

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
    
