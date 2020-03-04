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
 
#  TabbedWindow.py

# encodig: utf-8

import sys
import os
import traceback

from PyQt5.QtWidgets import *

sys.path.append('../')

from SOL4Py.ZApplicationView  import *
from SOL4Py.ZTabbedWindow  import *
from SOL4Py.ZScrolledImageView import *

class MainView(ZApplicationView):
                
  def __init__(self, name, x, y, width, height):
    super(MainView, self).__init__(name, x, y, width, height, Z.Vertical)
  
    self.tabbed = ZTabbedWindow(self, 0, 0, width, height)

    name1 = "../images/ClassicCar.png"
    self.widget1 = ZScrolledImageView(self, 0, 0, width, height)
    self.widget1.load_image(name1)
    self.tabbed.add(name1, self.widget1)

    name2 = "../images/DecisionTree.png"
    self.widget2 = ZScrolledImageView(self, 0, 0, width, height)
    self.widget2.load_image(name2)
    self.tabbed.add(name2, self.widget2)

    name3 = "./TabbedWindow.py"
    self.widget3 = QTextEdit("Time to say goodbye") 
    read_text = open(name3, 'r').read()
    self.widget3.setText(read_text)
    self.tabbed.add(name3, self.widget3)

    self.add(self.tabbed)
    
if main(__name__):

  try:
    name = os.path.basename(sys.argv[0])

    applet = QApplication(sys.argv)
    
    main_view  = MainView(name, 40, 40, 800, 400) 
    main_view.show ()

    applet.exec_()

  except:
     traceback.print_exc()
     pass

