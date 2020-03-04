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

# 2018/09/10
 
#  XGBRegressor.py
# This is based on the following program:
# http://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regression.html
#
# See also:
# xgboost/demo/guide-python/sklearn_examples.py
# https://github.com/dmlc/xgboost/blob/master/demo/guide-python/sklearn_examples.py

# encodig: utf-8

import sys
import os
import time

import traceback
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import pickle
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn import datasets
from sklearn.utils import shuffle
from sklearn.metrics import mean_squared_error

sys.path.append('../')
from SOL4Py.ZMLModel import *
from SOL4Py.ZApplicationView import *
from SOL4Py.ZLabeledComboBox import *
from SOL4Py.ZPushButton      import *
from SOL4Py.ZTabbedWindow    import *

from SOL4Py.ZVerticalPane    import *
from SOL4Py.ZTabbedWindow    import *
from SOL4Py.ZScalableScrolledFigureView import *


Boston   = 0
Diabetes = 1

############################################################
#
# XGBRegressorModel class
#
class XGBRegressorModel(ZMLModel):
   
  def __init__(self, dataset_id, mainv):
    super(XGBRegressorModel, self).__init__(dataset_id, mainv)
    
    
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
    if "feature_names" in attr:
      self.write("feature_names:" + str(self.dataset.feature_names))
    if "target_names" in attr:
      self.write("target_names:" + str(self.dataset.target_names))
  
    self.set_model_filename()
    self.view.description.setText(self.dataset.DESCR)
    
    X, y = self.dataset.data, self.dataset.target

    self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    self._end(self.load_dataset.__name__)
 
 
  def build(self):
    self._start(self.build.__name__)
    self.model = xgb.XGBRegressor()
    self._end(self.build.__name__)


  def train(self):
    #We use GridSearchCV
    self._start(self.train.__name__)
    start = time.time()
    
    params =  {'max_depth': [2,4,6], 'n_estimators': [50,100,200]}
    
    grid_search = GridSearchCV(self.model, params, verbose=1)
    grid_search.fit(self.X_train, self.y_train)
    self.write("GridSearch BestParams " + str(grid_search.best_params_) )
    self.write("GridSearch BestScore  " + str( grid_search.best_score_) )
    
    # Rebuild a XGBRegressor model by using grid_search.best_params_
    self.model = xgb.XGBRegressor(**grid_search.best_params_)
    self.model.fit(self.X_train, self.y_train)

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
    self.write("MSE:test  " +  str(mean_squared_error(self.y_test,  self.pred_test)) )


  def visualize(self):
   importances = pd.Series(self.model.feature_importances_, 
                               index = self.dataset.feature_names)
   importances = importances.sort_values()
   self.view.visualize(importances)

 
############################################################
#
# MainView class, which is a subclass of ZApplicationView
#
class MainView(ZApplicationView):  

  # MainView Constructor
  def __init__(self, title, x, y, width, height):
    super(MainView, self).__init__(title, x, y, width, height)
    self.font        = QFont("Arial", 10)
    self.setFont(self.font)
    
    # 1 Add a labeled combobox to top dock area
    self.add_datasets_combobox()
    
    # 2 Add a textedit to the left pane of the center area.
    self.text_editor = QTextEdit()
    self.text_editor.setFont(self.font)
    self.text_editor.setLineWrapColumnOrWidth(600)
    self.text_editor.setLineWrapMode(QTextEdit.FixedPixelWidth)

    self.description = QTextEdit()
    self.description.setFont(self.font)
    self.description.setLineWrapColumnOrWidth(600)
    self.description.setLineWrapMode(QTextEdit.FixedPixelWidth)

    # 3 Add a tabbled_window to the right pane of the center area.
    self.tabbed_window = ZTabbedWindow(self, 0, 0, width/2, height)
    
    # 4 Add a figure_view to the tabbed_window
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
    
    # We use the following datasets of sklearn to test XGBRegressor.
    self.datasets = {"Boston": Boston, "Diabetes": Diabetes}
    title = self.get_title()
    self.setWindowTitle( "Boston" + " - " + title)

    self.datasets_combobox.add_items(self.datasets.keys())
    self.datasets_combobox.add_activated_callback(self.datasets_activated)
    self.datasets_combobox.set_current_text(self.dataset_id)

    self.start_button = ZPushButton("Start", self)
    self.clear_button = ZPushButton("Clear", self)

    self.start_button.setFont(self.font)
    self.clear_button.setFont(self.font)
    
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
    self.model = XGBRegressorModel(self.dataset_id, self)
    self.start_button.setEnabled(False)    
    self.clear_button.setEnabled(False)
    try:
      self.model.run()
    except:
      pass
    self.start_button.setEnabled(True)
    self.clear_button.setEnabled(True)

    
  def file_new(self):
    self.text_editor.setText("")
    self.description.setText("")
    self.figure_view.hide()
    
    if plt.gcf() != None:  
      plt.close()

  
  def clear_button_activated(self, text):
    self.file_new()


  def visualize(self, importances):
    self.figure_view.show()
    if plt.gcf() != None:
      plt.close()

    importances.plot(kind = "barh")
    self.figure_view.set_figure( plt )


############################################################
#
# Program main start point
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
