#/******************************************************************************
# 
#  Copyright (c) 2018-2019 Antillia.com TOSHIYUKI ARAI. ALL RIGHTS RESERVED.
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
 
#  ScrolledImageView.py
 
# 2019/04/16 Updated to use ZApplicationView

# encodig: utf-8

import sys
import os
import traceback

import cv2
import errno

from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *

sys.path.append('../')

from SOL4Py.ZApplicationView            import *
from SOL4Py.ZScrolledImageView  import ZScrolledImageView

from SOL4Py.ZApplicationView  import *
from SOL4Py.ZImageView        import *
from SOL4Py.ZScaleComboBox    import *

class MainView(ZApplicationView):

  # MainView Constructor
  def __init__(self, title, x, y, width, height):
    super(MainView, self).__init__(title, x, y, width, height, Z.Vertical)
    self.image_view = ZScrolledImageView(self, 0, 0, width, height)
    filename = "../images/MeshedNioh.png"
    self.image_view.load_image(filename)
    self.add(self.image_view)
    self.set_filenamed_title(filename)
    
    self.show()


#*************************************************
#    
if main(__name__):
  try:
    app_name  = os.path.basename(sys.argv[0])
    applet    = QApplication(sys.argv)
  
    main_view = MainView(app_name, 40, 40, 500, 400)
    main_view.show ()

    applet.exec_()

  except:
    traceback.print_exc()
    
