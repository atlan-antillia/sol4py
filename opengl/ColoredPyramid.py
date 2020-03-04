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
 
#  ColoredPyramid.py

# encodig: utf-8

import sys

# 
sys.path.append('../')

from SOL4Py.opengl.ZOpenGLMainView import *
from SOL4Py.opengl.ZOpenGLObject import *

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

    def paintGL(self):
      glClear(GL_COLOR_BUFFER_BIT| GL_DEPTH_BUFFER_BIT)
      glClearColor(0.0, 0.0, 0.0, 0.0)
      glLoadIdentity()
      glTranslate(0.0, 0.0, -1.0) 
      gluLookAt(2.0, 4.0, 6.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
      glEnableClientState(GL_VERTEX_ARRAY) 
      glEnableClientState(GL_COLOR_ARRAY)

      vertices = [
        -0.5, -0.5, -0.5, 
         0.5, -0.5, -0.5, 
         0.5, -0.5,  0.5, 
        -0.5, -0.5,  0.5, 
         0.0,  0.5,  0.0, 
        ]
    
      #Colors(RGBAs) for the 5 vertices
      colors = [ 
        0.0, 0.0, 1.0, 1.0, 
        0.0, 1.0, 0.0, 1.0, 
        0.0, 0.0, 1.0, 1.0, 
        0.0, 1.0, 0.0, 1.0, 
        1.0, 0.0, 0.0, 1.0  
      ]
  
      #Indices for the 4 triangles.
      indices = [ 
        2, 4, 3,   
        1, 4, 2,   
        0, 4, 1,   
        4, 0, 3    
      ]
      avertices =  np.array(vertices, dtype="float32")
      acolors   =  np.array(colors, dtype="float32")
      
      glVertexPointer(3, GL_FLOAT, 0, avertices)
      glColorPointer (4, GL_FLOAT, 0, acolors)
      nindices     =  np.array(indices, dtype="uint32")

      glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, nindices)
      glDisableClientState(GL_VERTEX_ARRAY) 
      glDisableClientState(GL_COLOR_ARRAY)

      glFlush()

    def draw(self, vertices_list):
      for i in range(len(vertices_list)):
        v = vertices_list[i]
        glVertex3f(v[0], v[1], v[2])
 
 
    def resizeGL(self, width, height):
      side = min(width, height)
      if side < 0: return
      glViewport(0, 0, width, height)
      glMatrixMode(GL_PROJECTION)
      glLoadIdentity()
      gluPerspective(16.0, width / height, 0.5, 40.0)

      glMatrixMode(GL_MODELVIEW)


  ##Inner class ends
  
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

