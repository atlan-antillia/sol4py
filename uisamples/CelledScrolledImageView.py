﻿#/******************************************************************************
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
 
#  CelledScrolledImageView.py

# encodig: utf-8

import sys
import os
import cv2
import traceback

# 
sys.path.append('../')

from SOL4Py.ZApplicationView import *
from SOL4Py.ZScrolledImageView  import ZScrolledImageView
from SOL4Py.ZVerticalPane    import ZVerticalPane 
 
class MainView(ZApplicationView):

  # MainView Constructor
  def __init__(self, title, x, y, width, height):
    super(MainView, self).__init__(title, x, y, width, height)

    filename1 = "../images/flower.png"
    filename2 = "../images/flower3.jpg"
    
    # 1 Create the first imageview.
    self.image_views = [None, None]
    self.image_views[0] = ZScrolledImageView(self, 0, 0, width/2, height)

    # 2 Create the second imageview.
    self.image_views[1] = ZScrolledImageView(self, 0, 0, width/2, height)

    # 2 Add the image view to a main_layout of this main view.
    for i in range (len(self.image_views)):
       self.add(self.image_views[i])

    # 3 Load the file
    self.load_file(filename1, 0)
    self.load_file(filename2, 1)
      
    self.show()
  

  # Redefined add_file_menu.    
  def add_file_menu(self):
    # Typical file menu    
    self.file_menu = QMenu('&File', self)
    self.file_menu.addAction('&New',  self.file_new)
    self.file_menu.addAction('&Open First File', self.first_file_open)
    self.file_menu.addAction('&Open Second File', self.second_file_open)

    self.file_menu.addAction('&Save', self.file_save)
    self.file_menu.addAction('&Save As', self.file_save_as)
    self.file_menu.addAction('&Quit', self.file_quit)
    self.menuBar().addMenu(self.file_menu)
    
  # Show FileOpenDialog and select an image file.
  def first_file_open(self):
    self.file_open(0)

  def second_file_open(self):
    self.file_open(1)
    
  def file_open(self, index):
    options = QFileDialog.Options()
    filename, _ = QFileDialog.getOpenFileName(self,"FileOpenDialog", "",
                     "All Files (*);;Image Files (*.png;*jpg;*.jpeg)", options=options)
    if filename:
      self.load_file(filename, index)
      
  def load_file(self, filename, index):
    self.image_views[index].load_image(filename)    
    self.set_filenamed_title(filename)
      

#*************************************************
#    
if main(__name__):

  try:
    app_name  = os.path.basename(sys.argv[0])
    applet    = QApplication(sys.argv)
  
    main_view = MainView(app_name, 40, 40, 1000, 460)
    main_view.show ()

    applet.exec_()

  except:
    traceback.print_exc()


