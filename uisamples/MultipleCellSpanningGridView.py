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
 
#  GridLayoutOpenCVImageView.py
 
# 2018/05/01

# encodig: utf-8

import sys
import os
import traceback

import cv2
import errno

#from PyQt5.QtWidgets import *
#from PyQt5.QtGui     import *
#from PyQt5.QtCore    import *

sys.path.append('../')

from SOL4Py.ZApplicationView     import *
from SOL4Py.ZImageView           import *
from SOL4Py.opencv.ZOpenCVImageView     import *

#---------------------------------------------------------------------
#
if __name__ == '__main__':
  applet  = QApplication(sys.argv)
  appview = QWidget()
  appview.setWindowTitle(sys.argv[0])
  grid    = QGridLayout(appview)
  image_views = [None, None, None]
  filenames   = ["../images/Pedestrian.png", "../images/Pedestrian8.png", 
                 "../images/MenInWhite2.jpg"] 
                 #"../images/flower3.jpg",
                 #"../images/flower7.jpg"]

  flags = cv2.IMREAD_COLOR
  image_views[0] = ZOpenCVImageView(appview, filenames[0], flags)
  image_views[1] = ZOpenCVImageView(appview, filenames[1], flags) 
  image_views[2] = ZOpenCVImageView(appview, filenames[2], flags)
  
  grid.addWidget(image_views[0], 0, 0)
  grid.addWidget(image_views[1], 0, 1)
  grid.addWidget(image_views[2], 1, 0, 1, 2)
      
  
  
  appview.setGeometry(40, 40, 800, 400)
  appview.show()
  
  applet.exec_()

