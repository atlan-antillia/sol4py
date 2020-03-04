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
 
#  CheckImageTexturedCube.py

# encodig: utf-8

import sys
import numpy as np
import math

# 
sys.path.append('../')

from SOL4Py.opengl.ZOpenGLMainView import *
from SOL4Py.opengl.ZOpenGLTexturedSphere import *
from SOL4Py.opengl.ZCheckImage import *

class MainView(ZOpenGLMainView):
  ##--------------------------------------------
  class CheckImageTexturedSphere(ZOpenGLTexturedSphere):

    def __init__(self):
      ZOpenGLTexturedSphere.__init__(self, None, None, 1.0, 100, 100)
      check_image = ZCheckImage()
       
      self.bind()

      self.pixelStore(GL_UNPACK_ALIGNMENT, 1)
      self.parameter(GL_TEXTURE_MAG_FILTER, GL_NEAREST) 
      self.parameter(GL_TEXTURE_MIN_FILTER, GL_NEAREST) 

      self.env(GL_TEXTURE_ENV_MODE, GL_MODULATE)

      self.parameter(GL_TEXTURE_WRAP_S, GL_REPEAT)
      self.parameter(GL_TEXTURE_WRAP_T, GL_REPEAT)

      self.image(0, GL_RGBA, check_image.WIDTH, check_image.HEIGHT, 
                    0, GL_RGBA, GL_UNSIGNED_BYTE, check_image.data )
      self.unbind()

  ##
  class OpenGLView(ZOpenGLView):

    def __init__(self, parent=None):
      self.parent = parent
      super(ZOpenGLView, self).__init__(parent)


    def initializeGL(self):
      glEnable(GL_DEPTH_TEST)      
      glMatrixMode(GL_PROJECTION)
      glLoadIdentity()                    
      glMatrixMode(GL_MODELVIEW)
      
      self.texture = MainView.CheckImageTexturedSphere()


    def paintGL(self):
      glClear(GL_COLOR_BUFFER_BIT| GL_DEPTH_BUFFER_BIT)
      glClearColor(0.0, 0.0, 0.0, 0.0)
      glColor(1.0, 1.0, 1.0)
      glLoadIdentity()
      glTranslatef(0.0, 0.0, 0.0)
      gluLookAt(2.0, 6.0, 10.0, 0.0, 0.0, 0.0, 0.0, 10.0, 0.0) 
      #glEnable(GL_CULL_FACE);  
      #glCullFace(GL_BACK);
      glRotate(10.0, 1.0, 0.0, 0.0)
      
      self.texture.draw()
      
      glFlush()


    def resizeGL(self, width, height):
      side = min(width, height)
      if side < 0: return
      glViewport(0, 0, width, height)
      glMatrixMode(GL_PROJECTION)
      glLoadIdentity()
      gluPerspective(16.0, width / height, 0.5, 40.0)

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

