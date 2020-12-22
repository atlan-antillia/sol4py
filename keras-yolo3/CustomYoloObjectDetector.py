# Copyright 2020-2021 antillia.com Toshiyuki Arai
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#  CustomYoloObjectDetector.py
# See also: https://github.com/qqwweee/keras-yolo3

# encodig: utf-8

import sys
import os
import cv2
import traceback
import csv

# 
sys.path.append('../')

from SOL4Py.ZApplicationView import *

from SOL4Py.ZLabeledComboBox import ZLabeledComboBox
from SOL4Py.ZLabeledSlider   import ZLabeledSlider
from SOL4Py.opencv.ZOpenCVScrolledImageView import ZOpenCVScrolledImageView  
#from SOL4Py.opencv.ZOpenCVImageView import ZOpenCVImageView  

from SOL4Py.ZVerticalPane    import ZVerticalPane  
from SOL4Py.ZCSVTableView    import *


from CustomYolo import *

class MainView(ZApplicationView):
  # Inner classes
  #--------------------------------------------
  class DetectedImageView(ZOpenCVScrolledImageView):
  #class DetectedImageView(ZOpenCVImageView):
    def __init__(self, parent):
      ZOpenCVScrolledImageView.__init__(self, parent)
      
    def load(self, filename):
      self.load_opencv_image(filename)
             

  #--------------------------------------------
  

  # MainView Constructor
  def __init__(self, title, x, y, width, height):
    super(MainView, self).__init__(title, x, y, width, height)
    
    self.yolo = CustomYolo()
    
    filename = "../images/Pedestrian.png"
    
    # 1 Create a detected imageview.
    self.detected_image_view = self.DetectedImageView(self) 
  
    # 2 Add an image views to a main_layout of this main view.
    self.add(self.detected_image_view)
    
    # 3 Load the file
    self.load_file(filename)
    
    self.show()


  def __del__(self):
    print("Destructor __del__ called")
    if self.yolo != None:
      self.yolo.close_session()


  def file_open(self):
    options = QFileDialog.Options()
    filename, _ = QFileDialog.getOpenFileName(self,"FileOpenDialog", "",
                     "All Files (*);;Image Files (*.png;*jpg;*.jpeg)", options=options)
    if filename:
      self.load_file(filename)


  def add_control_pane(self, fixed_width=280):
    # Control pane widget
    self.vpane = ZVerticalPane(self, fixed_width)
    self.csv_tableview = ZCSVTableView(self)
    
    self.vpane.add(self.csv_tableview)
    self.set_right_dock(self.vpane)

  def load_csv_file(self, filename):
    # 1. Remove all rows from the self.model
    self.csv_tableview.clear()
    self.csv_tableview.load_file(filename)
    self.csv_tableview.strechLastSection(False)
    self.csv_tableview.resizeToContents(7) #len of ["id", "object", "score", "x", "y", "w", "h"]


  def load_file(self, filename):
    filename = os.path.abspath(filename)
    self.detected_image_view.load(filename)

    try:
      basename = os.path.basename(filename)

      save_imagefilename = os.path.join(os.getcwd(), "detected_" + basename)
      csv_filename       = os.path.join(os.getcwd(), basename + ".csv")
      
      print("SAVE FILENAME: " + save_imagefilename)
      print("CSV  FILENAME: " + csv_filename)

      image    = Image.open(filename)
      r_image  = self.yolo.detect_image(image, save_imagefilename, csv_filename)

      cv_image = np.asarray(r_image)
      cv_image = cv2.cvtColor(cv_image, cv2.COLOR_RGB2BGR)
      self.detected_image_view.set_opencv_image(cv_image)
      self.detected_image_view.update()
      self.load_csv_file(csv_filename)
      
      self.set_filenamed_title(filename)

    except:
      traceback.print_exc()


#*************************************************
#    
if main(__name__):
  try:
    app_name  = os.path.basename(sys.argv[0])
    applet    = QApplication(sys.argv)
  
    main_view = MainView(app_name, 40, 40, 1000, 380)
    main_view.show ()

    applet.exec_()

  except:
    traceback.print_exc()
    

