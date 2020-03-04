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
 
#  ColorPositioner.py

# encodig: utf-8

import sys
import os
import traceback

sys.path.append('../')

from SOL4Py.ZApplicationView  import *
from SOL4Py.ZColorPositioner import *

class MainView(ZApplicationView):
  # Inner classes
  #--------------------------------------------
  class ColorBox(QWidget):
    def __init__(self, parent):
      QWidget.__init__(self, parent)
      self.color = QColor(255, 128, 0)


    def paintEvent(self, event):
      painter = QPainter(self)
      painter.setBrush(self.color)
      painter.drawRect(20, 20, 200, 200)


    def update_color(self, r, g, b):
      self.color = QColor(r, g, b)
      self.update()


  # MainView Constructor
  def __init__(self, title, x, y, width, height):
    super(MainView, self).__init__(title, x, y, width, height)
    
    # 1 Create first imageview.
    self.colorbox = self.ColorBox(self)

    # 2 Add imageviews to the main_layout which is a horizontal layouter.
    self.add(self.colorbox)
    
    self.show()
  

  def add_control_pane(self, fixed_width=280):
    # Control pane widget
    print("add_control_pane")
    self.vpane = ZVerticalPane(self, fixed_width)
    self.positioner = ZColorPositioner(self)
    self.positioner.set_rgb_colors(255, 128, 0)
    
    self.vpane.add(self.positioner)
 
    self.positioner.add_value_changed_callback(self.slider_value_changed)
    
    self.set_right_dock(self.vpane)
 
 
  def slider_value_changed(self, value):
    values = self.positioner.get_values()
    self.colorbox.update_color(values[0], values[1], values[2])


#*************************************************
#    
if main(__name__):
  try:
    app_name  = os.path.basename(sys.argv[0])
    applet    = QApplication(sys.argv)
  
    main_view = MainView(app_name, 40, 40, 640, 380)
    main_view.show ()

    applet.exec_()

  except:
    traceback.print_exc()

