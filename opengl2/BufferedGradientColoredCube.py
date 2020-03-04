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
#    along with this program.  If not, see <http:#www.gnu.org/licenses/>.
#
#******************************************************************************/

#  BufferedGradientColoredBox.py

# encoding: utf-8

import sys
import os
import traceback

import traceback
import numpy as np
import math

sys.path.append('../')
from PIL import Image, ImageOps

from SOL4Py.opengl.ZOpenGLMainView import *
from SOL4Py.opengl.ZOpenGLColoredCube import *
from SOL4Py.openglarb.ZOpenGLBufferedShape import *

class MainView(ZOpenGLMainView):

  # Inner class starts.
  class OpenGLView(ZOpenGLView):
    ## Constructor
    def __init__(self, parent=None):
      self.parent = parent
      super(ZOpenGLView, self).__init__(parent)

     
    def initializeGL(self):

      colorsForEachVertex1 = [
        #face 1:
        [ 1.0, 0.0, 0.0], 
        [ 0.0, 1.0, 0.0], 
        [ 0.0, 0.0, 1.0], 
        [ 1.0, 1.0, 0.0],
        
        #face 2:
        [ 1.0, 0.0, 0.0], 
        [ 0.0, 1.0, 0.0], 
        [ 0.0, 0.0, 1.0], 
        [ 1.0, 1.0, 0.0],
        
        #face 3:
        [ 1.0, 0.0, 0.0], 
        [ 0.0, 1.0, 0.0], 
        [ 0.0, 0.0, 1.0], 
        [ 1.0, 1.0, 0.0],
        
        #face 4:
        [ 1.0, 0.0, 0.0], 
        [ 0.0, 1.0, 0.0], 
        [ 0.0, 0.0, 1.0], 
        [ 1.0, 1.0, 0.0],
        
        #face 5:
        [ 1.0, 0.0, 0.0], 
        [ 0.0, 1.0, 0.0], 
        [ 0.0, 0.0, 1.0], 
        [ 1.0, 1.0, 0.0],
        
        #face 6:
        [ 1.0, 0.0, 0.0], 
        [ 0.0, 1.0, 0.0], 
        [ 0.0, 0.0, 1.0], 
        [ 1.0, 1.0, 0.0],
      ];
      
      #cube1.setVerticesColors(colorsForEachVertex1) ##, CountOf(colorsForEachVertex1));
      cube1 = ZOpenGLColoredCube(colorsForEachVertex1, len(colorsForEachVertex1), 1.0)

      colorsForEachVertex2 = [
        #face 1:
        [ 0.0, 0.2, 0.4], 
        [ 0.4, 0.6, 0.8], 
        [ 0.8, 0.6, 0.4], 
        [ 0.4, 0.2, 0.0],
        
        #face 2:
        [ 0.0, 0.2, 0.4], 
        [ 0.4, 0.6, 0.8], 
        [ 0.8, 0.6, 0.4], 
        [ 0.4, 0.2, 0.0],
        
        #face 3:
        [ 0.0, 0.2, 0.4], 
        [ 0.4, 0.6, 0.8], 
        [ 0.8, 0.6, 0.4], 
        [ 0.4, 0.2, 0.0],
        
        #face 4:
        [ 0.0, 0.2, 0.4], 
        [ 0.4, 0.6, 0.8], 
        [ 0.8, 0.6, 0.4], 
        [ 0.4, 0.2, 0.0],
        
        #face 5:
        [ 0.0, 0.2, 0.4], 
        [ 0.4, 0.6, 0.8], 
        [ 0.8, 0.6, 0.4], 
        [ 0.4, 0.2, 0.0],
        
        #face 6:
        [ 0.0, 0.2, 0.4], 
        [ 0.4, 0.6, 0.8], 
        [ 0.8, 0.6, 0.4], 
        [ 0.4, 0.2, 0.0],
      ];
      cube2 = ZOpenGLColoredCube(colorsForEachVertex2, len(colorsForEachVertex2), 1.0)
      
      self.shape1 = ZOpenGLBufferedShape(cube1)
      self.shape2 = ZOpenGLBufferedShape(cube2)


    def paintGL(self):

      if self.shape1 != None and self.shape2 != None:
        glEnable( GL_DEPTH_TEST)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glClearColor(1.0, 1.0, 1.0, 1.0)

        #Draw the first shape1.
        glPushMatrix()
        glTranslate(-1.5,0.0,-1.0)  
        gluLookAt(2.0, 8.0, 15.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0) 
        self.shape1.draw()
        glPopMatrix()

        #Draw the second shape2.
        glPushMatrix()
        glTranslate(1.8, 0.0, -4.0)  
        gluLookAt(-4.0, -16.0, 20.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0) 
        self.shape2.draw()
        glPopMatrix()


    def resizeGL(self, w,  h):
   
      if w == 0 or h == 0:
        return
      
      glMatrixMode(GL_PROJECTION)
      glLoadIdentity()
      gluPerspective(16.0, w / h, 0.5, 40.0) 
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

    main_view = MainView(app_name, 40, 40, 600, 380)
    main_view.show ()

    applet.exec_()

  except:
    traceback.print_exc()

