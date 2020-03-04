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
 
#  ApplicationView.py

# encodig: utf-8

import sys
import os
import traceback

from PyQt5.QtWidgets import *

sys.path.append('../')

from SOL4Py.ZApplicationView  import *
from SOL4Py.ZImageView           import ZImageView

if main(__name__):

  try:
    name = os.path.basename(sys.argv[0])

    applet = QApplication(sys.argv)
    # Create an empty ZApplicationView 
    
    main_view  = ZApplicationView(name, 40, 40, 800, 400, layout=Z.Vertical) #layout=SOL.Vertical)
    image_view = ZImageView(None, 40, 40, 400, 300)
  
    image_view.load_image("../images/flower.png")
    main_view.add(image_view)
    
    main_view.show ()

    applet.exec_()

  except:
     traceback.print_exc()
     pass


