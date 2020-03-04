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

# MNISTImageView.py

import sys
import signal
import numpy as np
import traceback
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns


from PyQt5 import QtCore, QtWidgets, QtGui
from tensorflow import keras

from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *

sys.path.append('../')

from SOL4Py.ZApplicationView  import *
from SOL4Py.ZScrolledPlottingArea  import *


class MainView(ZApplicationView):
  # Constructor
  def __init__(self, title, x, y, width, height):
    super(MainView, self).__init__(title, x, y, width, height)
    
    self.plotter = ZScrolledPlottingArea(self, 1200, 1200)
    self.minist =  keras.datasets.mnist

    (self.X_train, self.y_train), (self.X_test_, self.y_test) = keras.datasets.mnist.load_data()

    self.class_names = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for i in range(25):
      plt.subplot(5,5,i+1)
      plt.xticks([])
      plt.yticks([])
      plt.grid(False)
      plt.imshow(self.X_train[i],  cmap=plt.cm.gray_r, interpolation="nearest")
      plt.xlabel(self.class_names[self.y_train[i]])
      
    self.add(self.plotter)
    
    self.show()

  def file_save(self):
    try:
      abs_current_path = os.path.abspath(os.path.curdir)
      files_types = "PDF (*.pdf);;PGF (*.pgf);;PNG (*.png);;PS (*.ps);;EPS (*.eps);;RAW (*.raw);;RGBA (*.rgba);;SVG (*.svg);;SVGZ (*.svgz)"
      filename, _ = QFileDialog.getSaveFileName(self, "FileSaveDialog", 
                             os.path.join(abs_current_path, "figure.png"),
                             files_types)
      if filename:
        plt.savefig(filename) 
    except:
      traceback.print_exc()
          
if main(__name__):

  try:
    name   = sys.argv[0]
    applet = QApplication(sys.argv)
    
    mainv = MainView(name, 40, 40, 800, 400)
    mainv.show()

    applet.exec_()
    
  except:
    traceback.print_exc()
    
