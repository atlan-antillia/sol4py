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
 
#  ZOpenGLColoredRegularIcosahedron.py

# encodig: utf-8
import sys
import numpy as np
import math

from ctypes import *

sys.path.append('../')

from SOL4Py.opengl.ZOpenGLMainView import *

from SOL4Py.opengl.ZOpenGLColoredRegularIcosahedron import *
from SOL4Py.openglarb.ZOpenGLBufferedShape import *


class MainView(ZOpenGLMainView):


  # Inner class starts.
  class OpenGLView(ZOpenGLView):
    ## Constructor
    def __init__(self, parent=None):
      self.parent = parent
      super(ZOpenGLView, self).__init__(parent)

    def initializeGL(self):

      glMatrixMode(GL_PROJECTION)
      glLoadIdentity()

      glEnable( GL_DEPTH_TEST)
      glFrustum(1 , -1 , -1 , 1 , 1 , 10)
      glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
      vertexColors = [
        [ 1.0, 0.0, 0.0],
        [ 0.0, 1.0, 0.0], 
        [ 0.0, 0.0, 1.0], 
        [ 1.0, 1.0, 0.0],
        [ 0.0, 1.0, 1.0],
        [ 1.0, 0.0, 1.0],
        [ 1.0, 0.0, 0.0],
        [ 0.0, 1.0, 0.0], 
        [ 0.0, 0.0, 1.0], 
        [ 1.0, 1.0, 0.0],
        [ 0.0, 1.0, 1.0],
        [ 1.0, 0.0, 1.0],        
      ]
      self.hedron = ZOpenGLColoredRegularIcosahedron(vertexColors, len(vertexColors))
      
      self.shape  = ZOpenGLBufferedShape(self.hedron)

    def paintGL(self):
      glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
      glLoadIdentity()
      glClearColor(0.0, 0.1, 0.2, 1.0)

      glPushMatrix()
      glTranslate(0.0,0.0,1.0)  
      gluLookAt(4.0, 12.0, 15.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0) 
      self.shape.draw()
      glPopMatrix()
 

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
    app_name  = os.path.basename(sys.argv[0])
    applet    = QApplication(sys.argv)
  
    main_view = MainView(app_name, 40, 40, 640, 480)
    main_view.show ()

    applet.exec_()

  except:
    traceback.print_exc()


