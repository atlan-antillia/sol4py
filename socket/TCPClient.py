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

# TCPClient.py

# Simple UDP Client

# encoding: utf-8

import socket
import sys
import traceback

class TCPClient:
  ##
  # Construcotr
  def __init__(self, ipaddress, port):

    # Create a stream socket.
    self.sock = None
    self.ipaddress = ipaddress
    self.port      = port

    try:
      self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
      self.sock.connect((ipaddress, port))
    except:
      traceback.print_exc()


  def run(self):
    self.val_loss  = 5.0
    self.val_acc   = 0.0
    self.count     = 10
    self.formatter = "{0:.4f}"

    for i in range(self.count):
      try:
        self.val_loss -= 0.02
        self.val_acc  +=  0.01
        fval_loss = self.formatter.format(self.val_loss)
        fval_acc  = self.formatter.format(self.val_acc)
        text = str(fval_loss) + ":" + str(fval_acc) + "\n"
        
        # Create a byte data from the text string.
        data = text.encode("utf-8")

        print('sending {!r}'.format(text))
        self.sock.send(data)

        data = self.sock.recv(1024)
        rtext = data.decode("utf-8")
        print('received {!r}'.format(rtext))

      except:
        traceback.print_exc()


  def close(self):
    if self.sock != None:
      self.sock.close()
      print("sock closed")



if __name__== "__main__":

  ipaddress = "127.0.0.1"
  port      = 7777
  if len(sys.argv) >= 2:
    ipaddress = str(sys.argv[1])
  if len(sys.argv) >= 3:
    port = int(sys.argv[2])
     
  client = TCPClient(ipaddress, port)

  try:
    client.run()
    
  except:
    traceback.print_exc()
  else:
    pass
  
  finally:
    client.close()

