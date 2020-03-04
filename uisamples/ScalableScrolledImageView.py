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
 
#  ScalableScrolledImageView.py

# encodig: utf-8

import sys
import os
import cv2
import traceback


#from PyQt5.QtCore    import *
#from PyQt5.QtWidgets import *
#from PyQt5.QtGui     import *

# 
sys.path.append('../')

from SOL4Py.ZApplicationView import *
from SOL4Py.ZScalableScrolledImageView  import *
from SOL4Py.ZVerticalPane    import * 
 
class MainView(ZApplicationView):

  # MainView Constructor
  def __init__(self, title, x, y, width, height):
    super(MainView, self).__init__(title, x, y, width, height)

    filename = "../images/flower.png"
    
    # 1 Create first imageview.
    self.image_view = ZScalableScrolledImageView(self, 0, 0, width, height)

    # 2 Add the image view to a main_layout of this main view.
    self.add(self.image_view)

    # 3 Load the file
    self.load_file(filename)
      
    self.show()


  # Show FileOpenDialog and select an image file.
  def file_open(self):
    options = QFileDialog.Options()
    filename, _ = QFileDialog.getOpenFileName(self,"FileOpenDialog", "",
                     "All Files (*);;Image Files (*.png;*jpg;*.jpeg)", options=options)
    if filename:
      self.load_file(filename)
      
  def load_file(self, filename):
    self.image_view.load_image(filename)    
    self.set_filenamed_title(filename)
      

#*************************************************
#    
if main(__name__):

  try:
    app_name  = os.path.basename(sys.argv[0])
    applet    = QApplication(sys.argv)
  
    main_view = MainView(app_name, 40, 40, 900, 380)
    main_view.show ()

    applet.exec_()

  except:
    traceback.print_exc()


