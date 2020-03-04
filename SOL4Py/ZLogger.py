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

 
#  ZLogger.py

#  See:  http://stackoverflow.com/questions/6810999/how-to-determine-file-function-and-line-number

# encodig: utf-8

import sys
import os
import inspect

import socket

from datetime import datetime

import traceback

#---------------------------------------------------------------------

class ZLogger:
  
  DEBUG    = 0
  INFO     = 1
  WARNING  = 2
  ERROR    = 3
  CRITICAL = 4
  LABELES  = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

  logger   = None
  
  ##
  # Constructor
  def __init__(self, ipaddress="127.0.0.1", port=5555):
    self.ipaddress = ipaddress
    self.port      = port
    self.level     = self.DEBUG
    self.stdout    = False
    self.sock      = None
    self.socketout = True
    self.fileout   = True
    self.filename  = None
    
    # Create a DATGRAM socket to send a log-string to a UDP LOG Server.
    try:
      self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      self.server_address = (ipaddress, port)
      print(self.server_address)
      ZLogger.logger = self

    except:
      print(formatted_traceback())


  def getLogger():
    if (ZLogger.logger == None):
      ZLogger.logger = ZLogger()
    return ZLogger.logger


  def setFilename(self, filename):
    self.filename = filename
    try:
      with open(self.filename, "a") as logFile:
        logFile.write("appended text")
    except:
      print(formatted_traceback())


  def setLevel(self, level):
    self.level = level


  ## 
  # Destructor
  def __del__(self):
    print("ZLogger.Destructor")
    self.close()


  #  See:  http://stackoverflow.com/questions/6810999/how-to-determine-file-function-and-line-number
  def getFrameInfo(self, stackIndex = 3):
    stack = inspect.stack()
    if stackIndex >= len(stack):
        return None
    callerframerecord = stack[stackIndex]
    frame = callerframerecord[0]
    return inspect.getframeinfo(frame)


  # Send a utf-8 decoded text to a udp log server. 
  def send(self, message, level):
    if self.level >=level:
      label = self.LABELES[level]
      dt    = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
      info  = self.getFrameInfo()

      if info != None:
        sinfo = info.filename + ': ' + str(info.lineno) + ': ' + info.function + ": "

        text = dt + ": " + label + ": " + sinfo + str(message)
        if self.stdout == True:
          print(text)
        if self.fileout == True and self.filename != None:
          try:
            with open(self.filename, "a") as logFile:
              logFile.write(text+ "\n")              
          except:
            # Ignore error
            pass
        if self.socketout == True:
          # You should send a "utf-8" encoded data
          data = text.encode("utf-8")
          self.sock.sendto(data, self.server_address)


  def debug(self, message):
    self.send(message, self.DEBUG)


  def info(self, message):
    self.send(message, self.INFO)


  def warning(self, message):
    self.send(message, self.WARNING)


  def error(self, message):
    self.send(message, self.ERROR)


  def critical(self, message):
    self.send(message, self.CRITICAL)


  def close(self):
    if self.sock != None:
      self.sock.close()
      self.sock = None



