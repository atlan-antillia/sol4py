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
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#******************************************************************************/

# 2019/04/26

#  LightedSphereOrbiter.py

# encodig: utf-8

import sys
import os
import math
import traceback

from PyQt5.Qt import QMutex

# 
sys.path.append('../')

from SOL4Py.opengl.ZOpenGLMainView import *
from SOL4Py.opengl.ZOpenGLTimerThread import *
from SOL4Py.opengl.ZOpenGLLight  import *
from SOL4Py.opengl.ZOpenGLMaterial  import *
from SOL4Py.opengl.ZOpenGLSphere  import *
from SOL4Py.opengl.ZOpenGLCircle  import *


class MainView(ZApplicationView):
  ##
  class OpenGLView(ZOpenGLView):
    CIRCLE_ANGLE = 360;
    INCREMENT    = 2;
   
    def __init__(self, parent=None):
      super(ZOpenGLView, self).__init__(parent)
      self.parent = parent

      self.angle = 0
      self.timerThread = None
      self.renderingInterval = 40
      self.mutex = QMutex()


    def initializeGL(self):
      self.quadric = ZOpenGLQuadric();
      self.quadric.drawStyle(GLU_FILL);
      self.quadric.normals(GLU_SMOOTH);
      self.sphere = ZOpenGLSphere(self.quadric, None, 0.5, 40, 40)
      self.circle = ZOpenGLCircle(0.0, 0.0, 0.0, 1.3);
      
      self.timerThread  = ZOpenGLTimerThread(self, self.renderingInterval);
      self.timerThread.start();


    def paintGL(self):
      self.mutex.lock()
      
      if (self.angle <(self.CIRCLE_ANGLE - self.INCREMENT) ):
          self.angle += self.INCREMENT;
      else:
        self.angle = self.INCREMENT;

      if (self.sphere != None):
        pos = self.circle.getOrbitPosition(self.angle);

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

        glLoadIdentity();
        gluLookAt(-5.0, 10.0, 4.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);

        glClearColor(0.0, 0.0, 0.0, 1.0);
        glEnable(GL_CULL_FACE); 
        glEnable(GL_LIGHTING);

        glTranslate(0.0, 0.0, 0.0);
        glColor(1.0, 1.0, 1.0); #green

        self.circle.draw();
       
        glTranslate(pos[0], pos[1], pos[2]);
        
        light = ZOpenGLLight (GL_LIGHT0);
        lightPosition = [-2.0, 0.0, -1.0, 1.0];  
        light.positionv(lightPosition);

        white = [1.0, 1.0, 1.0, 1.0];
        blue  = [0.0, 0.0, 1.0, 1.0];
        green = [0.0, 1.0, 0.0, 1.0];

        shininess = 100.0;

        material = ZOpenGLMaterial(GL_FRONT);
        material.diffusev(green);
        material.specularv(white);
        material.shininess(shininess);
       
        self.sphere.draw();
        
      self.mutex.unlock()


    def resizeGL(self, width, height):
      if width == 0 or height == 0:
        return;
       
      glViewport(0, 0, width, height)
      glMatrixMode(GL_PROJECTION)
      glLoadIdentity()
      gluPerspective(16.0, width / height, 0.5, 40.0); 
     
      glMatrixMode(GL_MODELVIEW);

  ##
  
  # MainView Constructor
  def __init__(self, title, x, y, width, height):
    super(MainView, self).__init__(title, x, y, width, height)

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
  
    main_view = MainView(app_name, 40, 40, 600, 440)
    main_view.show ()

    applet.exec_()

  except:
    traceback.print_exc()
