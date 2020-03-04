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
 
#  WebBrowser.py
 
# 2018/05/01

# encodig: utf-8

import sys
import os
import traceback

import cv2
import errno

from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWebEngineWidgets import QWebEngineView

sys.path.append('../')

from SOL4Py.ZApplicationView import *



class WebBrowser(ZApplicationView):
  def __init__(self, title, x, y, width, height):
    super(WebBrowser, self).__init__(title, x, y, width, height, Z.Vertical)

    self.web_view = QWebEngineView(self)
    self.combobox = QComboBox(self)
    self.combobox.setEditable(True)
    self.combobox.activated[str].connect(self.combobox_activated)
    self.add(self.combobox)
    self.add(self.web_view)
    self.show()

  def load(self, url):
    self.combobox.addItem(url)
    self.web_view.load(QUrl(url))
   
  def combobox_activated(self, text):
    self.web_view.load(QUrl(text))
    

#*************************************************
#    
if main(__name__):
  try:
    app_name  = os.path.basename(sys.argv[0])
    applet    = QApplication(sys.argv)
  
    web_browser = WebBrowser(app_name, 40, 40, 900, 380)
    web_browser.load("http://www.antillia.com") 
    web_browser.show ()

    applet.exec_()

  except:
     traceback.print_exc()
     pass

