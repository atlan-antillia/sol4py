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
 
# 2019/03/05
# 2019/09/13 Updated load_file method not to use a temporary image file.

#  VGG16Classifier.py

# encodig: utf-8

import sys
import os
import time
import traceback

from keras.utils import np_utils
from keras.preprocessing.image import load_img, img_to_array
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input 
from keras.applications.vgg16 import decode_predictions 
 
sys.path.append('../../')

from SOL4Py.ZImageClassifierView import *

DATASET_VGG16 = 0

############################################################
# Classifier View

class MainView(ZImageClassifierView):  
  # Class variables

  # ClassifierView Constructor
  def __init__(self, title, x, y, width, height):
    super(MainView, self).__init__(title, x, y, width, height,
               datasets={"VGG16": DATASET_VGG16})
    
    self.model_loaded = False
    self.image_size   = (224, 224)
    
    # keras.preprocessing.image
    self.image       = None

    #  Load trained model
    self.write("Loading VGG16 Model")
    self.model = VGG16()
    self.write("Loaded VGG16")
    self.model_loaded = True

    self.show()


  def load_file(self, filename):
    try:
      image_cropper = ZPILImageCropper(filename)
     
      # 1 Crop larget_central square region from an image of filename.
      cropped_image = image_cropper.crop_largest_central_square_region()
      
      # 2 Load an image from the cropped_fle.
      self.image_view.set_image(img_to_array(cropped_image)) 
      self.image_view.update_scale()

      self.set_filenamed_title(filename)
      
      # 3 Resize the cropped_image  
      self.image = cropped_image.resize(self.image_size)
      
      # 4 Convert the self.image to numpy ndarray and remove alpha channel.
      self.image = self.remove_alpha_channel(img_to_array(self.image))

      # 5 Set self.nadarryy to the test_image_view.
      self.test_image_view.set_image(self.image)
 
      # 6 Convert self.image(ndarray) to an input data format applicable to the VGG16 model.
      self.image = preprocess_input(self.image);
      
    except:
      self.write(formatted_traceback())


  def classify(self):
    self.write("------------------------------------------------------------")

    self.write("classify start")
    self.write(self.filename)
    input = np.stack([self.image]);
    
    predictions = self.model.predict(input)
    results = decode_predictions(predictions, top=5)[0]
    for result in results:
      self.write(str(result))

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
    
