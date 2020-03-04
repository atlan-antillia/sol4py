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
 
#  MaterializedSpheresRotationByKeyInput.py

# encodig: utf-8

import sys

# 
sys.path.append('../')

from SOL4Py.opengl.ZOpenGLMainView import *
from SOL4Py.opengl.ZOpenGLMultiTexturedCube import *
from SOL4Py.opengl.ZOpenGLLight import *
from SOL4Py.opengl.ZOpenGLMaterial import *
from SOL4Py.opengl.ZOpenGLSolidSphere import *
from SOL4Py.opengl.ZOpenGLWireSphere import *

class MainView(ZOpenGLMainView):
  ##--------------------------------------------
  class OpenGLView(ZOpenGLView):
    CUBES = 4
    
    def __init__(self, parent=None):
      self.parent = parent
      super(ZOpenGLView, self).__init__(parent)
      self.angle = 0


    def initializeGL(self):
      glEnable(GL_DEPTH_TEST)      
      glMatrixMode(GL_PROJECTION)
      glLoadIdentity()                    
      glMatrixMode(GL_MODELVIEW)
      black         = [ 0.0, 0.0, 0.0, 1.0 ]
      ambient       = [ 0.5, 0.5, 0.5, 1.0 ]
      diffuse       = [ 0.2, 0.4, 0.8, 1.0 ]
      specular      = [ 1.0, 1.0, 1.0, 1.0 ]
      emission      = [ 0.8, 0.0, 0.0, 0.0 ]

      lowShining    = [ 10.0 ]
      highShining   = [100.0 ]

      mat1 = ZOpenGLMateria(GL_FRONT, ambient, diffuse, specular, emission, lowShining)
      mat2 = ZOpenGLMateria(GL_FRONT, black,   diffuse, specular, black,    lowShining)
      mat3 = ZOpenGLMateria(GL_FRONT, black,   diffuse, black,    emission, highShining)
      mat4 = ZOpenGLMateria(GL_FRONT, ambient, diffuse, specular, black,    highShining)
      self.materias = [mat1, mat2, mat3, mat4]
      self.spheres = []
      for i in range(self.CUBES):
        if i%2 ==0:
          self.spheres.append(ZOpenGLWireSphere(self.materias[i], 0.5,  40, 40))
        else:
          self.spheres.append(ZOpenGLSolidSphere(self.materias[i], 0.5,  40, 40) )
 
      self.light =   ZOpenGLLight(GL_LIGHT0)
      self.light.position(10.0, 10.0, 10.0, 1.0)


    def paintGL(self):
      glClear(GL_COLOR_BUFFER_BIT| GL_DEPTH_BUFFER_BIT)
      glClearColor(0.0, 0.0, 0.0, 0.0)
      glLoadIdentity()
      glTranslatef(0.0, 0.0, -1.0)
      gluLookAt(2.0, 6.0, 10.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0) 
      glEnable(GL_CULL_FACE) 
      glEnable(GL_LIGHTING)
      for i in range(self.CUBES):
        glPushMatrix()
        glRotate(self.angle, 0.0, 1.0, 0.0)
        glTranslate(-2.0+1.3*i, 0.5,  0.0+ 0.3*i)
        self.spheres[i].draw()
        glPopMatrix()

      glFlush()

      
    def resizeGL(self, width, height):
      side = min(width, height)
      if side < 0: return
      glViewport(0, 0, width, height)
      glMatrixMode(GL_PROJECTION)
      glLoadIdentity()
      gluPerspective(16.0, width / height, 0.5, 40.0)

      glMatrixMode(GL_MODELVIEW)


    def keyPressEvent(self, event):
      if event.key() == Qt.Key_Left:
        self.angle = self.angle - 2.0
      if event.key() == Qt.Key_Right:
        self.angle = self.angle + 2.0
      
      self.update()
  ##--------------------------------------------


  # MainView Constructor
  def __init__(self, title, x, y, width, height):
    super(ZOpenGLMainView, self).__init__(title, x, y, width, height)

    # 1 Create first imageview.
    self.opengl_view = self.OpenGLView(self)

    # 2 Add the image view to a main_layout of this main view.
    self.add(self.opengl_view)
     
    self.show()


  def keyPressEvent(self, event):
    self.opengl_view.keyPressEvent(event)
    pass


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

