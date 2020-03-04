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
 
#  LabeledFileComboBox.py

# encodig: utf-8

import sys
import os
import traceback

from PyQt5.QtWidgets import *

sys.path.append('../')

from SOL4Py.ZApplicationView      import *
from SOL4Py.ZLabeledFileComboBox  import *
from SOL4Py.ZLabeledFileComboBox  import *

class MainView(ZApplicationView):
  # Constructor
  def __init__(self, name, x, y, w, h):
    ZApplicationView.__init__(self, name, x, y, w, h)

    self.file_combobox = ZLabeledFileComboBox(self, "FileComboBox")
    self.file_combobox.add_clicked_callback(self.folder_button_clicked)    
    self.file_combobox.add_activated_callback(self.combobox_activated)

    self.file_combobox.listup_files("../images/*.png")
    
    self.set_top_dock(self.file_combobox)

    self.box = QWidget(self)
    self.setCentralWidget(self.box)
    
    self.show()
    
  def folder_button_clicked(self):
    dir = QFileDialog.getExistingDirectory(self,
                                               'OpenFolder',
                                               os.path.expanduser('.'),
                                               QFileDialog.ShowDirsOnly)
    if dir:
      #dir = dir.replace('/', os.sep)
      print("Folder button clicked {}".format(dir))
      self.file_combobox.listup_files(dir+ "/*.png")

  def combobox_activated(self, text):
    print("combobox activated: {}".format(text))
    fullpath = self.file_combobox.get_current_text_as_fullpath()
    print("current item as fullpath {}".format(fullpath))
    
    pass

      
if main(__name__):

  try:
    name = os.path.basename(sys.argv[0])

    applet = QApplication(sys.argv)
    # Create an empty ZApplicationView 
    
    main_view  = MainView(name, 40, 40, 800, 400) #
    main_view.show ()

    applet.exec_()

  except:
     traceback.print_exc()
     pass


