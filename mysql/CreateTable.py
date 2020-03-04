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

# encoding: utf-8

# CreateTable.py

# 2020/01/30

import sys
import os
import configparser

sys.path.append('../')

from SOL4Py.ZMain  import *

from SOL4Py.mysql.ZMySQLDB  import *

"""
create table test.User (
  id             bigint unsigned not null primary key auto_increment,
  auth_token     varchar(40)    default NULL,          
  email          varchar(255)   unique default NULL,
  password       varchar(512)   default NULL,     #AES ENCRUPTED Password 
  validated      bool           default False,     
  last_modified  datetime       default NOW()
);

"""
if main(__name__):
  # Commandline parameters user password dabase
      
  db = ZMySQLDB(argv=sys.argv)
  try:
    #Create test database.
    create_db  = "CREATE DATABASE IF NOT EXISTS test"
    db.execute(create_db)

    #Create test.User table

    create_tbl = "CREATE TABLE IF NOT EXISTS test.User ( "\
                 + " id             bigint unsigned not null primary key auto_increment, "\
                 + " auth_token     varchar(40)    default NULL, "\
                 + " email          varchar(255)   unique default NULL, "\
                 + " password       varchar(512) default NULL, "\
                 + " last_modified  datetime       default NOW() "\
                 + " ); "
    
    db.execute(create_tbl)
    db.commit()
    print("Created test.user Table")
             
        
  except Exception as ex:
    print("Exception {}".format(ex))

  finally:
    db.connection.close()

  