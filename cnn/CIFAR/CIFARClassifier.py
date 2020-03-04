#/******************************************************************************
# 
#  Copyright (c) 2018 Antillia.com TOSHIYUKI ARAI. ALL RIGHTS RESERVED.
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
 
# 2018/09/20
# 2019/09/13 Updated load_file method not to use a temporary image file.

# On CIFAR-10 dataset, see the following page:

# http://www.cs.toronto.edu/~kriz/cifar.html

# See also:
# https://github.com/ageron/tensorflow-models/blob/master/slim/datasets/download_and_convert_cifar.py

#  CIFARClassifier.py

# encodig: utf-8

import sys
import os
import time
import traceback

sys.path.append('../../')

from SOL4Py.ZImageClassifierView import *

from CIFARModel import *

CIFAR10  = 0
CIFAR100 = 1

############################################################
# Classifier View

class MainView(ZImageClassifierView):  
  # Class variables

  # ClassifierView Constructor
  def __init__(self, title, x, y, width, height):
    super(MainView, self).__init__(title, x, y, width, height,
                datasets = {"CIFAR10": CIFAR10, "CIFAR100": CIFAR100})
    
    self.model_loaded = False
    self.image_size = (32, 32)
    
    self.class_names_set = [None, None]
    
    # keras.preprocessing.image
    self.image       = None
                        
    # The names of the classes.
    # See https://github.com/ageron/tensorflow-models/blob/master/slim/datasets/download_and_convert_cifar.py
    
    self.class_names_set[CIFAR10] = [ 
                'airplane','automobile', 'bird',     'cat',    'deer',
                'dog',     'frog',       'horse',    'ship',   'truck',]

    self.class_names_set[CIFAR100] = [
                'apple',      'aquarium_fish', 'baby',       'bear',         'beaver',
                'bed',        'bee',           'beetle',     'bicycle',      'bottle',
                'bowl',       'boy',           'bridge',     'bus',          'butterfly',
                'camel',      'can',           'castle',     'caterpillar',  'cattle',
                'chair',      'chimpanzee',    'clock',      'cloud',        'cockroach',
                'couch',      'crab',          'crocodile',  'cup',          'dinosaur',
                'dolphin',    'elephant',      'flatfish',   'forest',       'fox',
                'girl',       'hamster',       'house',      'kangaroo',     'keyboard',
                'lamp',       'lawn_mower',    'leopard',    'lion',         'lizard',
                'lobster',    'man',           'maple_tree', 'motorcycle',   'mountain',
                'mouse',      'mushroom',      'oak_tree',   'orange',       'orchid',
                'otter',      'palm_tree',     'pear',       'pickup_truck', 'pine_tree',
                'plain',      'plate',         'poppy',      'porcupine',    'possum',
                'rabbit',     'raccoon',       'ray',        'road',         'rocket',
                'rose',       'sea',           'seal',       'shark',        'shrew',
                'skunk',      'skyscraper',    'snail',      'snake',        'spider',
                'squirrel',   'streetcar',     'sunflower',  'sweet_pepper', 'table',
                'tank',       'telephone',     'television', 'tiger',        'tractor',
                'train',      'trout',         'tulip',      'turtle',       'wardrobe',
                'whale',      'willow_tree',   'wolf',       'woman',        'worm',]

    # 6 Load trained model
    
    self.model = CIFARModel(self.dataset_id, mainv=self)
    
    if self.model.is_trained():
      self.model.load_dataset()
      self.model.create()
      self.model.load()    # Load a trained weight
      self.model.compile()
      self.model.evaluate()
      self.model_loaded = True
    else:
      print("You have to create a model file and weight file")
      print("Please run: python CIFARModel.py " + str(self.dataset_id))
      QMessageBox.warning(self, "MNIST", 
           "Model/Weight File Missing.\nPlease run: python CIFARModel.py " + str(self.dataset_id))

    self.show()


  def datasets_activated(self, text):
    self.dataset_id = self.datasets[text]
    title = self.get_title()
    self.setWindowTitle(text + " - " + title)

    self.classifier_button.setEnabled(False)
    print("dataset_id {}".format(self.dataset_id))
    self.model.set_dataset_id(self.dataset_id)
    self.model.load_dataset()
    
    if self.model.is_trained():
      self.model.create()    # Recreate the model because it depends on self.mode.nclasses 
    
      self.model.load()
      self.model.compile()
      self.model.evaluate()
      self.model_loaded = True
      
    else:
      self.model.build()
      
      print("You have to create a model file and weight file")
      print("Run: python CIFARModel.py " + str(self.dataset_id))
      QMessageBox.warning(self, "CIFAR", 
           "Model/Weight File Missing.\nPlease run: python CIFARModel.py " + str(self.dataset_id))
 

  def classify(self):
    self.write("------------------------------------------------------------")

    self.write("classify start")
    self.write(self.filename)

    prediction = self.model.predict(self.image)
    
    pred = np.argmax(prediction, axis=1)
    #self.write("Prediction: index " + str(pred))
    class_names = self.class_names_set[self.dataset_id]
        
    if pred >0 or pred <len(class_names):
      self.write("Prediction:" + class_names[int(pred)])
      
    self.write("classify end")
      
   
############################################################
#    
if main(__name__):

  try:
    app_name  = os.path.basename(sys.argv[0])
    applet    = QApplication(sys.argv)
  
    main_view = MainView(app_name, 40, 40, 900, 500)
    main_view.show ()

    applet.exec_()

  except:
    traceback.print_exc()
    
