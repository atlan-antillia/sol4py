﻿#/******************************************************************************
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

# 2020/01/30
# See also https://stackoverflow.com/questions/5241031/python-inserting-and-retrieving-binary-data-into-mysql

# encoding: utf-8
0
# UpdateTableThread.py



"""
create table test.User (
  id             bigint unsigned not null primary key auto_increment,
  auth_token     varchar(40)    default NULL,          
  email          varchar(255)   unique default NULL,
  password       varchar(512)   default NULL,      #(AES IV) + (AES ENCRUPTED Password) 
  validated      bool           default False,     
  last_modified  datetime       default NOW()
);

"""


import sys
import os
import configparser

sys.path.append('../')

from SOL4Py.ZMain  import *
import base64

from SOL4Py.mysql.ZMySQLDB  import *
from SOL4Py.mysql.ZThreadedMySQLConnection  import *
from SOL4Py.crypto.ZAESIVEmbeddedCipher import *
from SOL4Py.generator.ZTokenGenerator import *
from SOL4Py.generator.ZEmailAddressGenerator import *
from SOL4Py.generator.ZPasswordGenerator import *


# Define your own thread class derived from ZThreadedMySQLConnection.

class DeleteFromTableThread(ZThreadedMySQLConnection):
  def __init__(self, connection):
    super().__init__(connection)

  # Define your own thread procedure 
  def run(self):
    try:
      delete = "DELETE FROM test.User WHERE email LIKE %s"
      values = ('%.jp', )
      self.cursor.execute(delete, values)
      self.commit()
 
      select = "SELECT *  FROM test.User WHERE email LIKE %s"
      values = ('%.jp',)
      
      rows = db.execute_fetchall(select, values)
      if rows != None:
         print("Rows len {}".format(len(rows)) )
      else:
         print("Selected None")
             
    except:
       traceback.print_exc()
       self.rollback()


if main(__name__):
  # user password database 
  
  db = ZMySQLDB(argv=sys.argv)
   
  try:
    delete_thread = DeleteFromTableThread(db.connection)
    delete_thread.start()
    delete_thread.join()
 
  except:
     traceback.print_exc()
  
  finally:
    db.connection.close()
 
  
  