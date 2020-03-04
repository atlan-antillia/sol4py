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
 
#  FolderBrowser.py
 
# encodig: utf-8

import sys
import os
import traceback

import errno

sys.path.append('../')

from SOL4Py.ZApplicationView import *


class MainView(ZApplicationView):
  def __init__(self, title, x, y, width, height):
    super(MainView, self).__init__(title, x, y, width, height, Z.Vertical)
 
    self.model = QFileSystemModel()
    self.model.setRootPath("")
    self.treeview = QTreeView()
    self.treeview.setModel(self.model)
 
    self.treeview.setAnimated(False)
    self.treeview.setIndentation(20)

    self.add(self.treeview)
    
    self.treeview.clicked.connect(self.clicked)
    self.treeview.doubleClicked.connect(self.doubleClicked)

    self.show()


  def doubleClicked(self, index):
    #QModelIndex index
    file_path=self.model.filePath(index)
    print("doubleClicked: " + file_path)
    self.set_filenamed_title(file_path)


  def clicked(self, index):
    #QModelIndex index
    file_path=self.model.filePath(index)
    print("clicked: " + file_path)
    self.set_filenamed_title(file_path)
        

#*************************************************
#    
if main(__name__):

  try:
    app_name  = os.path.basename(sys.argv[0])
    applet    = QApplication(sys.argv)
  
    main_view = MainView(app_name, 40, 40, 640, 480)
    main_view.show ()

    applet.exec_()

  except:
    traceback.print_exc()

