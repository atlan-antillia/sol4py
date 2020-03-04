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
#    but WITHOUT ANY WARRANTY without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#******************************************************************************/
 
#  Torus.py

# encodig: utf-8

import sys
import numpy as np

# 
sys.path.append('../')
from PIL import Image, ImageOps

from SOL4Py.opengl.ZOpenGLMainView import *
from SOL4Py.opengl.ZOpenGLLight import *
from SOL4Py.opengl.ZOpenGLMaterial import *
from SOL4Py.opengl.ZOpenGLGeometry import *

class MainView(ZOpenGLMainView):
  ##--------------------------------------------
  class OpenGLView(ZOpenGLView):

    def __init__(self, parent=None):
      self.parent = parent
      super(ZOpenGLView, self).__init__(parent)

    def paintGL(self):
      glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
      glLoadIdentity()
      gluLookAt(2.0, 4.0, 8.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

      glClearColor(0.0, 0.0, 0.0, 1.0)
      glEnable(GL_CULL_FACE) 
      glEnable(GL_LIGHTING)

      glEnable(GL_DEPTH_TEST)     
      light = ZOpenGLLight(GL_LIGHT0)
      light.position(10.0, 10.0, 10.0, 1.0)

      material = ZOpenGLMaterial(GL_FRONT)
      material.specular(1.0, 1.0, 1.0, 1.0) 
      material.shininess(100.0) 

      geometry = ZOpenGLGeometry(None)
      glPushMatrix()
      material.diffuse(0.0, 0.0, 1.0, 1.0)  
      glTranslate(-1.0, -2.0, -6.0)
      glRotate(-40.0, 1.0, 0.0, 0.0)
      geometry.wireTorus(1.0, 1.8, 10, 50)
      glPopMatrix()


    def resizeGL(self, width, height):
      side = min(width, height)
      if side < 0: return
      glViewport(0, 0, width, height)
      glMatrixMode(GL_PROJECTION)
      glLoadIdentity()
      r = width/height
      glFrustum(-r, r, -1.0, 1.0, 2.0, 100.0);

      glMatrixMode(GL_MODELVIEW)
  ##--------------------------------------------
  
  
  # MainView Constructor
  def __init__(self, title, x, y, width, height):
    super(ZOpenGLMainView, self).__init__(title, x, y, width, height)

    # 1 Create first imageview.
    self.opengl_view = self.OpenGLView(self)

    # 2 Add the image view to a main_layout of this main view.
    self.add(self.opengl_view)

    self.show()



#*************************************************
#    
if main(__name__):

  try:
    glutInit(sys.argv)
    app_name  = os.path.basename(sys.argv[0])
    applet    = QApplication(sys.argv)
  
    main_view = MainView(app_name, 40, 40, 600, 380)
    main_view.show ()

    applet.exec_()

  except:
    traceback.print_exc()

