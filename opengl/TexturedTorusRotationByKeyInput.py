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
#    along with this program.  If not, see <http:# www.gnu.org/licenses/>.
#
#******************************************************************************/

#  TexturedTorusRotationByKeyInput.py

# encodig: utf-8

import sys

# 
sys.path.append('../')

from SOL4Py.opengl.ZOpenGLMainView import *
from SOL4Py.opengl.ZOpenGLLight import *
from SOL4Py.opengl.ZOpenGLMaterial import *
from SOL4Py.opengl.ZOpenGLTexturedTorus import *
from SOL4Py.opengl.ZOpenGLSphere import *
from SOL4Py.opengl.ZOpenGLQuadric import *
from SOL4Py.opengl.ZOpenGLMateria import *

class MainView(ZOpenGLMainView):
  ##--------------------------------------------
  class OpenGLView(ZOpenGLView):
    
    def __init__(self, parent=None):
      self.parent = parent
      super(ZOpenGLView, self).__init__(parent)
      self.angle = 0


    def initializeGL(self):
      self.light =   ZOpenGLLight(GL_LIGHT0)
      self.torus   = None
      
      filename = "../images/Nanten.png"
 
      self.createTexture(filename)
      self.parent.set_filenamed_title(filename)
      self.axis = [-10.0, -10.0, 80.0]


    def paintGL(self):
      glClear(GL_COLOR_BUFFER_BIT| GL_DEPTH_BUFFER_BIT)
      glClearColor(1.0, 1.0, 1.0, 0.0)
      glLoadIdentity()
      glEnable(GL_CULL_FACE)
      glCullFace(GL_BACK)

      gluLookAt(2.0, 2.0, 4.0, 0.0, 0.0, 0.0, 0.0, 10.0, 0.0)

      glEnable(GL_LIGHTING)

      glTranslatef(0.0, 0.0, 0.0)
      glRotate(self.angle, self.axis[0], self.axis[1], self.axis[2])
      light = ZOpenGLLight (GL_LIGHT0)
      lightPosition = [15.0, 25.0, -25.0, 1.0]  
      light.positionv(lightPosition)

      white = [1.0, 1.0, 1.0, 1.0]
      blue  = [0.0, 0.0, 1.0, 1.0]
      green = [0.0, 1.0, 0.0, 1.0]
      shininess = 100.0

      material = ZOpenGLMaterial(GL_FRONT)
      material.diffusev(white)
      material.specularv(blue)
      material.shininess(shininess)
       
      if self.torus != None:
        self.torus.draw()


    def resizeGL(self, width, height):
      if width == 0 or height == 0:
        return
      glViewport(0, 0, width, height)
      glMatrixMode(GL_PROJECTION)
      glLoadIdentity()
      glFrustum(width / height, -width / height, -1.0, 1.0, 2.0, 40.0)
      glMatrixMode(GL_MODELVIEW)
 

    def keyPressEvent(self, event):
      if event.key() == Qt.Key_Left:
        self.angle = self.angle - 2.0
      if event.key() == Qt.Key_Right:
        self.angle = self.angle + 2.0
      
      self.update()


    def createTexture(self, filename):
      self.torus = ZOpenGLTexturedTorus(filename, None, 0.3, 0.6, 50, 40)

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

  # Show FileOpenDialog and select an image file.
  def file_open(self):
    options = QFileDialog.Options()
    filename, _ = QFileDialog.getOpenFileName(self,"FileOpenDialog", "",
                     "All Files (*);;Image Files (*.png;*jpg;*.jpeg)", options=options)
    if filename:
      self.load_file(filename)


  def load_file(self, filename):
    self.opengl_view.createTexture(filename)    
    self.set_filenamed_title(filename)


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

