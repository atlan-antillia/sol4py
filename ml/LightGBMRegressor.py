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
 
# 2018/09/01

# This is based on the following program:
# https://github.com/Microsoft/LightGBM/blob/master/examples/python-guide/sklearn_example.py

#  LightGBMRegressor.py

# encodig: utf-8

import sys
import os
import time
import traceback
import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt
import numpy as np

import pickle
import lightgbm as lgb

from sklearn.model_selection import train_test_split
#from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn import datasets
from sklearn.utils import shuffle
from sklearn.metrics import mean_squared_error
from sklearn.metrics import confusion_matrix, classification_report

sys.path.append('../')

from SOL4Py.ZMLModel         import *
from SOL4Py.ZApplicationView import *
from SOL4Py.ZLabeledComboBox import *
from SOL4Py.ZPushButton      import *
from SOL4Py.ZVerticalPane    import * 
from SOL4Py.ZTabbedWindow    import *
from SOL4Py.ZScalableScrolledFigureView import *

Boston   = 0
Diabetes = 1

############################################################
# Classifier Model clas

class LightGBMRegressorModel(ZMLModel):

  ##
  # Constructor
  def __init__(self, dataset_id, mainv):
    super(LightGBMRegressorModel, self).__init__(dataset_id, mainv)
          
  def run(self):
    self.write("====================================")
    self._start(self.run.__name__)
    try:    
      self.load_dataset()
      
      if self.trained():
        self.load()
      else:
        self.build()
        self.train()
        self.save()
        
      self.predict()
      self.visualize()
    except:
      traceback.print_exc()
    
    self._end(self.run.__name__)
     
     
  def load_dataset(self):
    self._start(self.load_dataset.__name__)

    if self.dataset_id == Boston:
       self.dataset= datasets.load_boston()
       self.write("loaded Boston dataset")
    if self.dataset_id == Diabetes:
       self.dataset= datasets.load_diabetes()
       self.write("loaded Diabetes dataset")
    attr = dir(self.dataset)
    self.write("dir:" + str(attr))
    if "target_names" in attr:
      self.write("target names:" + str(self.dataset.target_names))
    if "feature_names" in attr:
      self.write("feature names:" + str(self.dataset.feature_names))
  
    self.set_model_filename()
    self.view.description.setText(self.dataset.DESCR)
    
    X, y = self.dataset.data, self.dataset.target

    #X, y = shuffle(self.dataset.data, self.dataset.target, random_state=13)
    self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.3, random_state=42)
 
    self._end(self.load_dataset.__name__)
 
 
  def build(self):
    self._start(self.build.__name__)
    self.model = lgb.LGBMRegressor(
                        objective='regression',
                        num_leaves=31,
                        n_estimators=30)
                        
    self._end(self.build.__name__)


  def train(self):  
    self._start(self.train.__name__)
    start = time.time()
    
    # Class fit method of the regressor
    self.model.fit(self.X_train, self.y_train,
                eval_set=[(self.X_test, self.y_test)],
                eval_metric='rmse',
                early_stopping_rounds=5,
                verbose=1)
    elapsed_time = time.time() - start
    elapsed = str("Train elapsed_time:{0}".format(elapsed_time) + "[sec]")
    self.write(elapsed)

    self._end(self.train.__name__)


  def predict(self):
    self._start(self.predict.__name__)
    self.pred_train = self.model.predict(self.X_train)
    self.pred_test  = self.model.predict(self.X_test)
    self.mean_squared_error()

    self._end(self.predict.__name__)

  def mean_squared_error(self):
    self.write("MSE:train " +  str(mean_squared_error(self.y_train, self.pred_train)) )
    self.write("MSE:test  " + str( mean_squared_error(self.y_test,  self.pred_test)) )


  def visualize(self):
   importances = pd.Series(self.model.feature_importances_, 
                               index = self.dataset.feature_names)
   importances = importances.sort_values()
   self.view.visualize(importances)
    

############################################################
# Classifier View

class MainView(ZApplicationView):  
  # Class variables

  # ClassifierView Constructor
  def __init__(self, title, x, y, width, height):
    super(MainView, self).__init__(title, x, y, width, height)
    self.font        = QFont("Arial", 10)
    self.setFont(self.font)
    
    # 1 Add a labeled combobox to top dock area
    self.add_datasets_combobox()
    
    # 2 Add a text_editor to the left pane of the center area.
    self.text_editor = QTextEdit()
    self.text_editor.setLineWrapColumnOrWidth(600)
    self.text_editor.setLineWrapMode(QTextEdit.FixedPixelWidth)

    # 3 Add a tabbed_window to the right pane of the center area.
    self.tabbed_window = ZTabbedWindow(self, 0, 0, width/2, height)

    # 4 Add a description text edit to the tabbed_window
    self.description = QTextEdit()
    self.description.setLineWrapColumnOrWidth(600)
    self.description.setLineWrapMode(QTextEdit.FixedPixelWidth)
    
    # 5 Add a figure_view to the tabbed_window.
    self.figure_view = ZScalableScrolledFigureView(self, 0, 0, width/2, height)   
    self.add(self.text_editor)
    self.add(self.tabbed_window)
    
    self.tabbed_window.add("Description", self.description)
    self.tabbed_window.add("Importances", self.figure_view)
    self.figure_view.hide()
 
    self.show()
    
    
  def add_datasets_combobox(self):
    self.dataset_id = Boston
    self.datasets_combobox = ZLabeledComboBox(self, "Datasets", Qt.Horizontal)
    self.datasets_combobox.setFont(self.font)
    
    # We use the following datasets of sklearn to test XGBClassifier.
    self.datasets = {"Boston": Boston, "Diabetes": Diabetes}
    title = self.get_title()
    self.setWindowTitle( "Boston" + " - " + title)
    
    self.datasets_combobox.add_items(self.datasets.keys())
    self.datasets_combobox.add_activated_callback(self.datasets_activated)
    self.datasets_combobox.set_current_text(self.dataset_id)

    self.start_button = ZPushButton("Start", self)
    self.clear_button = ZPushButton("Clear", self)
    
    self.start_button.add_activated_callback(self.start_button_activated)
    self.clear_button.add_activated_callback(self.clear_button_activated)

    self.datasets_combobox.add(self.start_button)
    self.datasets_combobox.add(self.clear_button)
    
    self.set_top_dock(self.datasets_combobox)
  
      
  def write(self, text):
    self.text_editor.append(text)
    self.text_editor.repaint()

    
  def datasets_activated(self, text):
    self.dataset_id = self.datasets[text]
    title = self.get_title()
    self.setWindowTitle(text + " - " + title)


  def start_button_activated(self, text):
    self.model = LightGBMRegressorModel(self.dataset_id, self)
    self.start_button.setEnabled(False)    
    self.clear_button.setEnabled(False)
    try:
      self.model.run()
    except:
      pass
    self.start_button.setEnabled(True)
    self.clear_button.setEnabled(True)
        

  def clear_button_activated(self, text):
    self.text_editor.setText("")
    self.description.setText("")
    
    self.figure_view.hide()
    #if plt.gcf() != None:  
    plt.close()


  def visualize(self, importances):
    self.figure_view.show()
    # Close a plotter to restart a new plotting.
    plt.close()

    plt.tight_layout()
    importances.plot(kind = "barh")
    self.figure_view.set_figure(plt)
  
  
############################################################
#    
if main(__name__):

  try:
    app_name  = os.path.basename(sys.argv[0])
    applet    = QApplication(sys.argv)
  
    main_view = MainView(app_name, 40, 40, 800, 500)
    main_view.show ()

    applet.exec_()

  except:
    traceback.print_exc()
    
