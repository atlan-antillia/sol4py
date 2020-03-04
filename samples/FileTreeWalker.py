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
 
# 2019/05/17
# FileTreeWalker.py

# encodig: utf-8

import os
import sys
import socket
import glob

import traceback

sys.path.append('../')

from SOL4Py.ZMain    import *
from SOL4Py.ZLogger import *

logger = ZLogger(ipaddress="127.0.0.1", port=5555)
logger.socketout = True
logger.stdout    = True
logger.fileout   = True

logger.setLevel(ZLogger.ERROR)


class FileTreeWalker:
  ##
  #
  def __init__(self, base_dir="./"):
    logger.info("Constructor.base_dir " + base_dir)
    self.base_dir = base_dir


  def run(self):
    logger.info("start:" + self.base_dir)
    self.walk(self.base_dir)
    logger.info("end")


  def walk(self, folder):
    logger.info("started")
    try:
      if os.path.isdir(folder):
        subfolders = sorted( os.listdir(folder) )

        for index, subfolder in enumerate(subfolders):
          dir = os.path.join(folder, subfolder)
          logger.info("dir: " + dir)

          files = glob.glob(dir + "/*")
          for i, file in enumerate(files):
           logger.info("file:" + file)
           
          # Call self.walk recursively
          self.walk(dir)
      else:
        logger.error("Not dir {}".format(folder))
    except:
      logger.error(formatted_traceback())
      
    
    logger.info("end")


############################################################
#    

if main(__name__):
  base = "./"
  
  try:
    if (len(sys.argv) ==2):
      base = sys.argv[1]
      
    app_name  = os.path.basename(sys.argv[0])
    logger.filename = app_name + ".log"
    
    walker = FileTreeWalker(base)
    walker.run()

  except:
    logger.error(formatted_traceback())
    
    traceback.print_exc()

  
