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
 
#  MultipleScrolledFigureViewer.py

# encodig: utf-8

import sys
import os
import cv2
import traceback

import seaborn as sns
from sklearn import datasets
import matplotlib.pyplot as plt

from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *

# 
sys.path.append('../')

from SOL4Py.ZApplicationView import *
from SOL4Py.ZScrolledFigureView  import ZScrolledFigureView
from SOL4Py.ZVerticalPane    import ZVerticalPane 
 
class MainView(ZApplicationView):

  # MainView Constructor
  def __init__(self, title, x, y, width, height):
    super(MainView, self).__init__(title, x, y, width, height)
    
    # 1 Create three figure view.
    self.image_views = [None, None, None]
    num = len(self.image_views)

    for i in range(num):
      self.image_views[i] = ZScrolledFigureView(self, 0, 0, width/num, height)
      self.add(self.image_views[i])

    # 2 Set plt figures
    self.set_figures()
    
    self.show()

  def set_figures(self):
    # 1 Flight heatmap
    sns.set()
    plt.title("Flights Heatmap")
    flights = sns.load_dataset("flights")
    flights = flights.pivot("month", "year", "passengers")
    sns.heatmap(flights, annot=True, fmt="d")
    plt.tight_layout()
    self.image_views[0].set_figure(plt)
    
    # 2 Iris pairplot
    iris = sns.load_dataset("iris")
    sns.set()
    sns.pairplot(iris, hue="species", size=3.0)
    plt.title("Iris Pairplot")

    self.image_views[1].set_figure(plt)    

    # 3 Iris swarmplot
    plt.title("Iris Swarmplot")
    sns.set()
    sns.swarmplot(x="species", y="petal_length", data=iris)
    
    self.image_views[2].set_figure(plt)    


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


