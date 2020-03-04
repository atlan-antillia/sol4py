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

# 2018/09/30

# Simple Nonblocking TCP Socket Server thread example
# CustomNonblockingTCPServerThread.py


# encoding: utf-8

import os
import sys
import traceback
import socket
import threading
import time

sys.path.append('../')

from SOL4Py.ZMain                        import *
from SOL4Py.network.ZClientRequestHandlerThread  import *
from SOL4Py.network.ZNonblockingTCPServerThread  import *


##
#
# Nonblocking TCP Socket Server thread
#
class CustomNonblockingTCPServerThread(ZNonblockingTCPServerThread):

  ##--------------------------------------------------------
  # Inner class starts.
  # Inner thread class to handle a communiation with a client 
  
  class ClientRequestHandlerThread(ZClientRequestHandlerThread):
    ## 
    # Construcotr
    def __init__(self, client_sock, address, server_sock):
      super(CustomNonblockingTCPServerThread.ClientRequestHandlerThread, self).__init__(client_sock, address, server_sock)


    def handle_request(self, data):
       print("Recv from client: {} {}".format(self.client, data.decode("utf-8")))
       reply = "Reply from server: {}".format(self.server_sock)
       self.client.send(reply.encode("utf-8"))

  ## Inner class ends.
  ##--------------------------------------------------------
  

  ##
  # Constructor
  def __init__(self, host, port):
    super(CustomNonblockingTCPServerThread, self).__init__(host, port)


  def create_request_handler_thread(self, client, address, server_sock):
    thread = CustomNonblockingTCPServerThread.ClientRequestHandlerThread(client, address, self.sock)
    thread.start()


##
#
if main(__name__):

  ipaddress = "127.0.0.1"
  port      = 7777
  if len(sys.argv) >= 2:
    ipaddress = str(sys.argv[1])
  if len(sys.argv) >= 3:
    port = int(sys.argv[2])

  try:
    server = CustomNonblockingTCPServerThread(ipaddress, port)
    server.start()

    # To catch KeyboardInterrupt exception, we use the following while loop.
    while True:
      time.sleep(1)

  except (KeyboardInterrupt, SystemExit):
    print("Caught an exception")

  except:
    traceback.print_exc()

  finally:
    server.stop()
    print("Server stopped")
    exit()

