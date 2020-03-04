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
 
# 2019/05/29
# 2019/09/13 Updated load_file method not to use a temporary image file.

#  RoadSignslassifier.py

# encodig: utf-8

import sys
import os
import time
import traceback

sys.path.append('../../')

from SOL4Py.ZImageClassifierView import *

from RoadSignsModel import *


############################################################
# Classifier View

class MainView(ZImageClassifierView):  
  # Class variables

  # ClassifierView Constructor
  def __init__(self, title, x, y, width, height):
    super(MainView, self).__init__(title, x, y, width, height,
                     datasets={"RoadSigns": 0})
    
    self.model_loaded = False
    self.image_size = (RoadSignsModel.IMAGE_WIDTH, RoadSignsModel.IMAGE_HEIGHT)
        
    # Target image to be classified by this classifer.
    self.image       = None
    
    self.classes = self.get_class_names()
    
    self.model = RoadSignsModel(self.dataset_id, mainv=self)
    if self.model.is_trained():
      self.model.create()
      
      # Load trained model provided trained.
      self.model.load()
      self.model.compile()
      #self.model.evaluate()
      self.model_loaded = True
    else:
      print("You have to create a model file and weight file")
      print("Please run: python ImageModel.py " + str(self.dataset_id))
      QMessageBox.warning(self, "RoadSignsClassifier", 
           "Model/Weight File Missing.\nPlease run: python RoadSignsModel.py " + str(self.dataset_id))

    self.show()


  def classify(self):
    self.write("------------------------------------------------------------")
    self.write("classify start")
    self.write(self.filename)
    prediction = self.model.predict(self.image)
    
    # Get top five pairs of score and classname 
    result = self.get_top_five(prediction, self.classes)
    self.write("Predictions:")
    for score, name in result:
      self.write("  {:.4f}  {}".format(score, name))

    self.write("classify end")


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
    
