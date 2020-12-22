# Copyright 2020-2021 antillia.com Toshiyuki Arai
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

#  ImageView.py

# encodig: utf-8

import sys
import os
import traceback

from PyQt5.QtWidgets import *

sys.path.append('../')

from SOL4Py.ZApplicationView  import *
from SOL4Py.ZImageView           import ZImageView

if main(__name__):

  try:
    name = os.path.basename(sys.argv[0])

    applet = QApplication(sys.argv)
    # Create an empty ZApplicationView 
    
    main_view  = ZApplicationView(name, 40, 40, 800, 400, layout=Z.Vertical) #layout=SOL.Vertical)
    image_view = ZImageView(None, 40, 40, 400, 300)
  
    image_view.load_image("../images/flower.png")
    main_view.add(image_view)
    
    main_view.show ()

    applet.exec_()

  except:
     traceback.print_exc()
     pass


