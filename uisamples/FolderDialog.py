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
 
#  ApplicationViewiew.py

# encodig: utf-8

import sys
import os
import traceback


sys.path.append('../')

from SOL4Py.ZApplicationView  import *
from SOL4Py.ZLabeledFileComboBox import ZLabeledFileComboBox


class MainView(QMainWindow):
  # Constructor
  def __init__(self, name):
     QMainWindow.__init__(self)
     self.setWindowTitle(name)
     self.hbox = QWidget(self)
     self.hlayout = QHBoxLayout(self.hbox)
     self.hlayout.setAlignment(Qt.AlignRight)
     self.label   = QLabel("          ", self.hbox)
     self.label.setMinimumWidth(300)
     self.label.setMaximumWidth(300)
     
     self.pushb = QPushButton("...", self.hbox)
     
     self.pushb.clicked.connect(self.button_clicked)
     
     self.hlayout.addWidget(self.label)
     self.hlayout.addWidget(self.pushb)     
     self.setCentralWidget(self.hbox)

  def button_clicked(self):
    dir = QFileDialog.getExistingDirectory(self,
                                               'OpenFolder',
                                               os.path.expanduser('.'),
                                               QFileDialog.ShowDirsOnly)
    if dir:
      #dir = dir.replace('/', os.sep)
      print("Folder button clicked {}".format(dir))
      self.label.setText(dir)
         
if main(__name__):

  try:
    name = os.path.basename(sys.argv[0])

    applet = QApplication(sys.argv)
        
    main_view  = MainView(name)
    main_view.setGeometry(40, 40, 600, 100)
 
    main_view.show ()

    applet.exec_()

  except:
    traceback.print_exc()


