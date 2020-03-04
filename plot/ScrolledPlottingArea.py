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

# ScrolledPlottingArea.py

import sys
import signal
import numpy as np
import traceback
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

from numpy.random import rand

from PyQt5 import QtCore, QtWidgets, QtGui

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
    
    self.plotter = ZScrolledPlottingArea(self, 1200, 500)
    
    self.ax1= self.plotter.add(131)
    self.ax1.hist(rand(100), bins=20, color='k', alpha=0.3)
    
    self.ax2= self.plotter.add(132)
    self.ax2.scatter(np.arange(30), np.arange(30) + 3 * rand(30))

    self.ax3 = self.plotter.add(133)
    
    sns.set()
    uniform_data = np.random.rand(100, 100)
    sns.heatmap(uniform_data, ax = self.ax3)

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
    
