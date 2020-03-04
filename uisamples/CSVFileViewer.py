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
 
#  CSVFileViewer.py

# encodig: utf-8

import sys
import os
import traceback
import csv


sys.path.append('../')

from SOL4Py.ZApplicationView  import *
from SOL4Py.ZCSVTableView  import *

class MainView(ZApplicationView):
                
  def __init__(self, name, x, y, width, height):
    super(MainView, self).__init__(name, x, y, width, height, Z.Vertical)
    self.csv_tableview = ZCSVTableView(self)
    self.add(self.csv_tableview)
    self.csv_tableview.load_file("../data/iris.csv")
    
    self.show()


  def load_file(self, filename):
    # 1. Remove all rows from the self.model
    self.csv_tableview.clear()
    self.csv_tableview.load_file(filename)


  def file_new(self):
    msg = "Are you sure you want to clear the table-view?"
    reply = QMessageBox.question(self, "Confirmation", 
                     msg, QMessageBox.Yes, QMessageBox.No)
    if reply == QMessageBox.Yes:
      # 1. Remove all rows from the self.model
      self.csv_tableview.clear()

   
  def file_open(self):
    options = QFileDialog.Options()
    filename, _ = QFileDialog.getOpenFileName(self,"FileOpenDialog", "",
                     "All Files (*);;Image Files (*.csv)", options=options)
    if filename:
      self.load_file(filename)

      self.set_filenamed_title(filename)


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
