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

# SelectFromTableThread.py


# 2020/01/30

# encoding: utf-8

"""
create table test.User (
  id             bigint unsigned not null primary key auto_increment,
  auth_token     varchar(40)    default NULL,          
  email          varchar(255)   unique default NULL,
  password       varchar(512) default NULL,      #AES ENCRUPTED Password 
  validated      bool           default False,     
  last_modified  datetime       default NOW()
);

"""


import sys
import os
import traceback
import configparser

sys.path.append('../')

from SOL4Py.ZMain  import *

from SOL4Py.mysql.ZMySQLDB  import *
from SOL4Py.mysql.ZThreadedMySQLConnection  import *

from SOL4Py.crypto.ZAESIVEmbeddedCipher import *

# Define your own thread class derived from ZThreadedMySQLConnection.

class SelectFromTableThread(ZThreadedMySQLConnection):
  def __init__(self, connection):
    super().__init__(connection)

  
  def run(self):
    try:
      select = "SELECT id, auth_token, email, password FROM test.User WHERE email LIKE %s OR email LIKE %s"
      values = ('%.com', '%.info')
      
      self.cursor.execute(select, values)

      rows = self.cursor.fetchall()
      
      for row in rows:
        (id, auth_token, email, hex_iv_password) = row
        cipher = ZAESIVEmbeddedCipher(ZCipher.AS_HEX)

        key    = email
        decrypted = cipher.decrypt(hex_iv_password, key)
        
        utf8_decrypted = decrypted.decode('utf-8')
        print("id  {}".format(id))
        print("auth_token {}".format(auth_token))
        print("email      {}".format(email))
        print("password   {}".format(utf8_decrypted))
      
      self.commit()
      
    except:
       traceback.print_exc()
       self.rollback()


if main(__name__):
  # user passwd database 
  
  db = ZMySQLDB(argv=sys.argv)
   
  try:
    selection_thread = SelectFromTableThread(db.connection)
    selection_thread.start()
    selection_thread.join()
 
  except:
     traceback.print_exc()
  
  finally:
    db.connection.close()
 
  