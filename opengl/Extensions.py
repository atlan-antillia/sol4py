﻿# Copyright 2020-2021 antillia.com Toshiyuki Arai
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#  Extensions.py

# encodig: utf-8

import sys

# 
sys.path.append('../')

from SOL4Py.opengl.ZOpenGLMainView import *
from SOL4Py.opengl.ZOpenGLExtension import *
from SOL4Py.ZListView import *

class MainView(ZOpenGLMainView):
  ##--------------------------------------------
  class OpenGLView(ZOpenGLView):

    def __init__(self, parent=None):
      self.parent = parent
      super(ZOpenGLView, self).__init__(parent)


    def initializeGL(self):
      glEnable(GL_DEPTH_TEST)      
      glMatrixMode(GL_PROJECTION)
      glLoadIdentity()                    
      glMatrixMode(GL_MODELVIEW)
      self.extension = ZOpenGLExtension()
      extensions = self.extension.get_extensions()
      self.parent.add_extensions(extensions)
      

    def paintGL(self):
      glClear(GL_COLOR_BUFFER_BIT| GL_DEPTH_BUFFER_BIT)
      glClearColor(0.0, 0.0, 1.0, 1.0)
      glLoadIdentity()
      glTranslatef(0.0, 0.0, 0.0)

      glBegin(GL_TRIANGLES)
      self.coloredVertex(1.0, 0.0, 1.0, 0.0, 0.0)
      self.coloredVertex(0.5, 0.5, 1.0, -1.0, 0.9)
      self.coloredVertex(0.0, 0.0, 0.0, 1.0, 0.9)

      self.coloredVertex(1.0, 0.0, 0.0, 0.0, 0.0)
      self.coloredVertex(0.0, 0.5, 0.0, -1.0, -0.9)
      self.coloredVertex(1.0, 1.0, 0.0, 1.0, -0.9)
      glEnd()

      glFlush()


    def resizeGL(self, width, height):
      side = min(width, height)
      if side < 0: return
      glViewport(0, 0, width, height)
      glMatrixMode(GL_PROJECTION)
      glLoadIdentity()
      glMatrixMode(GL_MODELVIEW);

    def coloredVertex(self, r, g, b, x, y):  
      glColor3f(r, g, b)
      glVertex2f(x, y)
  
  ##--------------------------------------------


  # MainView Constructor
  def __init__(self, title, x, y, width, height):
    super(ZOpenGLMainView, self).__init__(title, x, y, width, height)

    # 1 Create first imageview.
    self.opengl_view = self.OpenGLView(self)

    # 2 Add the image view to a main_layout of this main view.
    self.add(self.opengl_view)

    self.show()


  # Add control pane to MainView
  def add_control_pane(self, fixed_width=240):
    self.vpane = ZVerticalPane(self, fixed_width)
    self.label = QLabel("GL_EXTENSIONS")
    self.vpane.add(self.label)
    
    self.list_view = ZListView(self)
    self.vpane.add(self.list_view)
     
    self.set_right_dock(self.vpane)


  def add_extensions(self, extensions):
     for extension in extensions:
      self.list_view.add_item(extension)


#*************************************************
#    
if main(__name__):

  try:
    app_name  = os.path.basename(sys.argv[0])
    applet    = QApplication(sys.argv)
  
    main_view = MainView(app_name, 40, 40, 600, 300)
    main_view.show ()

    applet.exec_()

  except:
    traceback.print_exc()

