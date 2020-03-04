#/******************************************************************************
# 
#  Copyright (c) 2020 Antillia.com TOSHIYUKI ARAI. ALL RIGHTS RESERVED.
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

# ZThreadedMySQLConnection.py

# 2020/01/30

# encoding: utf-8

# pip install mysql-connector-python

import sys
import os
import configparser

import threading
import mysql

import mysql.connector

class ZThreadedMySQLConnection(threading.Thread):
  
  ## Constructor
  def __init__(self, connection):
    super().__init__()
    self.connection = connection
    if self.connection == None:
      raise Exception("ZThreadedMySQLConnection: Invalid connection")
      
    self.cursor     = self.connection.cursor()
    if self.cursor == None:
      raise Exception("ZThreadedMySQLConnection: Failed to get cursor from connection")

  ## Destructor
  def __del__(self):
    try:
      if self.cursor != None:
        self.cursor.close()
        self.cusor = None
    except:
      pass
      
    
  def commit(self):
    self.connection.commit()
    

  def rollback(self):
    self.connection.rollback()
    
