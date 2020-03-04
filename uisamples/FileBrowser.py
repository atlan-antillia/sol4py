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
 
#  FileBrowser.py
 
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

    self.treeview = QTreeView()
    self.model = QFileSystemModel(self.treeview)
    self.model.setReadOnly(False)
    root = self.model.setRootPath("/")
    self.treeview.setModel(self.model)
    self.treeview.setRootIndex(root)

    self.add(self.treeview)
    
    self.treeview.clicked.connect(self.clicked)
    self.treeview.doubleClicked.connect(self.doubleClicked)

    self.show()


  def doubleClicked(self, signal):
    print(signal)
    #QModelIndex index
    file_path=self.model.filePath(signal)
    print("doubleClicked: " + file_path)


  def clicked(self, index):
    print(index)
    #QModelIndex index
    file_path=self.model.filePath(index)
    print("clicked: " + file_path)
        

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


class Browser(QWidget):
    def __init__(self):
        super(Browser, self).__init__()
        self.treeview = QTreeView()
        self.model = QFileSystemModel(self.treeview)
        self.model.setReadOnly(False)
        root = self.model.setRootPath("/")
        self.treeview.setModel(self.fileSystemModel)
        self.treeview.setRootIndex(root)

        Layout = QVBoxLayout(self)
        Layout.addWidget(self.treeView)
        self.setLayout(Layout)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Browser()
    main.show()
    sys.exit(app.exec_())