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
 
#  Triangle.py

# encodig: utf-8

import sys

# 
sys.path.append('../')

from SOL4Py.opengl.ZOpenGLMainView import *

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
      glTranslatef(-1.5, 0.0, -6.0)

      glBegin(GL_QUADS)
      #Front
      self.redVertex  ( 0.0,  1.0, 0.0)
      self.greenVertex(-1.0, -1.0, 1.0)
      self.blueVertex ( 1.0, -1.0, 1.0)
 
      # Right
      self.redVertex  (0.0,  1.0,  0.0)
      self.blueVertex (1.0, -1.0,  1.0)
      self.greenVertex(1.0, -1.0, -1.0)
 
      # Back
      self.redVertex  ( 0.0,  1.0,  0.0)
      self.greenVertex( 1.0, -1.0, -1.0)
      self.blueVertex (-1.0, -1.0, -1.0)
 
      # Left
      self.redVertex  ( 0.0,  1.0,  0.0)
      self.blueVertex (-1.0, -1.0, -1.0)
      self.greenVertex(-1.0, -1.0,  1.0)
        
      glEnd()
      glFlush()

      
    def resizeGL(self, width, height):
      side = min(width, height)
      if side < 0: return
      glViewport(0, 0, width, height)
      glMatrixMode(GL_PROJECTION)
      glLoadIdentity()
      gluPerspective(50.0, width / height, 0.1, 50.0)

      glMatrixMode(GL_MODELVIEW)


    def redVertex(self, x, y, z):
      glColor3f(1.0, 0.0, 0.0)  
      glVertex3f(x, y, z)

    def greenVertex(self, x, y, z):
      glColor3f(0.0, 1.0, 0.0)  
      glVertex3f(x, y, z)

    def blueVertex(self, x, y, z):
      glColor3f(0.0, 0.0, 1.0)  
      glVertex3f(x, y, z)

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

